import aiohttp
import asyncio
import time

async def start_timer(session, trace_config_ctx, params):
    trace_config_ctx.start_time = time.time()

async def log_response_metadata(session, trace_config_ctx, params):
    latency = time.time() - trace_config_ctx.start_time
    print(f"url={params.url} method={params.method} status={params.response.status} latency={latency}")


trace_config = aiohttp.TraceConfig()
trace_config.on_request_start.append(start_timer)
trace_config.on_request_end.append(log_response_metadata)

async def main():
    async with aiohttp.ClientSession(
            trace_configs = [trace_config]) as session:
        async with session.get('https://github.com') as resp:
            print('HTTP Response: ', resp.status)


asyncio.run(main())
