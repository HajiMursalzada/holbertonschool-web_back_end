#!/usr/bin/env python3
"""Basic async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Basic async"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
