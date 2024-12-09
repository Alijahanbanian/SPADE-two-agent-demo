from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
import spade

class ChildAgent(Agent):
    class CalculateSumBehaviour(OneShotBehaviour):
        async def run(self):
            msg = await self.receive(timeout=10)
            if msg:
                numbers = map(int, msg.body.split(","))
                result = sum(numbers)
                reply_ans = msg.make_reply()
                reply_ans.body = str(result)
                await self.send(reply_ans)
                print(f"ChildAgent: Sent result {result} to ParentAgent")
            else:
                print("ChildAgent: No message received.")

    async def setup(self):
        self.add_behaviour(self.CalculateSumBehaviour())

class ParentAgent(Agent):
    class ParentBehaviour(OneShotBehaviour):
        async def run(self):
            child_agent = ChildAgent("Child@localhost", "password")
            await child_agent.start(auto_register=True)
            print("ParentAgent: ChildAgent started")
            msg = Message(to="Child@localhost") 
            msg.body = "7,12"         
            await self.send(msg)
            reply = await self.receive(timeout=10)
            print(f"ParentAgent: Result: {reply.body}" if reply else "ParentAgent: No reply received.")
            await child_agent.stop()
            print("ParentAgent: ChildAgent stopped")
            await self.agent.stop()
            print("ParentAgent finished !!!")
    async def setup(self):
        print("ParentAgent started ...")
        self.add_behaviour(self.ParentBehaviour())

async def main():
    parent_agent = ParentAgent("Parent@localhost", "password")
    await parent_agent.start(auto_register=True)
    await spade.wait_until_finished(parent_agent)
spade.run(main())