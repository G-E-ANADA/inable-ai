from langchain_aws import ChatBedrock
import asyncio
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()

class AI_CLAUDE_MODEL:
    ANTHROPIC_VERSION = os.environ["ANTHROPIC_VERSION"]
    MODEL_ID = os.environ["MODEL_ID"]

    def __init__(self):
        self.model_id = self.MODEL_ID
        self.anthropic_version = self.ANTHROPIC_VERSION

    def set_model_id(self, model_id: str):
        self.model_id = model_id


class AI:

    def __init__(self
                 , model: AI_CLAUDE_MODEL = AI_CLAUDE_MODEL()
                 , max_tokens: int = 2048
                 , temperature: float = 0
                 , region_name: str = os.environ["BEDROCK_REGION"]
                 , streaming: bool = True):
        self.model_kwargs = {
            "anthropic_version": model.anthropic_version,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        self.region_name = region_name
        self.streaming = streaming
        self.model_id = model.model_id
        self.llm = self.get_llm()

    def set_max_tokens(self, max_tokens: int):
        if max_tokens > 0:
            self.model_kwargs["max_tokens"] = max_tokens
        else:
            raise ValueError("Max tokens must be positive")

    def set_temperature(self, temperature: float):
        if 0.0 <= temperature <= 1.0:
            self.model_kwargs["temperature"] = temperature
        else:
            raise ValueError("Temperature must be between 0.0 and 1.0")

    def set_region_name(self, region_name: str):
        self.region_name = region_name

    def set_streaming(self, streaming: bool):
        self.streaming = streaming

    def get_llm(self):
        return ChatBedrock(
        model_id=self.model_id,
        model_kwargs=self.model_kwargs,
        region_name=self.region_name,
        streaming=self.streaming,
    )

    async def run_gen_ai(self, user_query, summary_data):
        llm = self.llm

        first_prompt = f"""
        <request>
            <instruction>
                당신은 장애인 구인구직 서비스인 Inable 서비스의 고객지원 봇 입니다. 
                유저의 질문은 <user_query></user_query> 안에 있습니다. 
                만약, <user_query></user_query> 있는 내용이 장애인 구인구직의 내용과 관련이없다고 판단된다면, 다시 질문달라고 요청하세요.
            </instruction>
            <user_query>{user_query}</user_query>
            <job_post_summary>{summary_data}</job_post_summary>
        </request>
        """

        messages = [HumanMessage(content=first_prompt)]

        response_content = ""
        buffer = ""

        async for chunk in llm.astream(messages):
            chunk_content = chunk.content if hasattr(chunk, "content") else str(chunk)

            response_content += chunk_content
            buffer += chunk_content

            buffer_replaced = buffer.replace("\n", "<br/>")
            yield f"data: {buffer_replaced}\n\n"
            # print(buffer)
            buffer = ""

            await asyncio.sleep(0.03)

        buffer_replaced = buffer.replace("\n", "<br/>")
        if buffer:
            yield f"data: {buffer_replaced}\n\n"
            # print(buffer)

        # save_ai_response(chat_logs[0]["user_id"], response_content)

        yield "event: close\n\n"
