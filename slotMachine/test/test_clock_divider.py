import cocotb
import cocotb.triggers
import cocotb.clock
import random

import cocotb.utils
from cocotb_test.simulator import run
import pytest
import glob

@cocotb.test()
async def clockDivider_tb(dut):
    # 50 MHz clock period
    period_50MHz = 20

    clk_50MHz = cocotb.clock.Clock(dut.clk, period_50MHz, 'ns')
    print("hello")
    await cocotb.start(clk_50MHz.start())

    # 25 MHz clock period
    period_25MHz = 40
    dut.speed.value = 25000000
    dut.rst.value = 1

    prev_time = None
    
    for i in range(10):
        await cocotb.triggers.RisingEdge(dut.clk_div)
        current_sim_time = cocotb.utils.get_sim_time()
        if prev_time != None:
            assert prev_time + period_25MHz == current_sim_time, f"Failed to generate clock with period {period_25MHz}ns"
        prev_time = current_sim_time

    # 25 MHz clock period
    period_10MHz = 100
    dut.speed.value = 10000000
    dut.rst.value = 1

    prev_time = None
    
    for i in range(10):
        await cocotb.triggers.RisingEdge(dut.clk_div)
        current_sim_time = cocotb.utils.get_sim_time()
        if prev_time != None:
            assert prev_time + period_10MHz == current_sim_time, f"Failed to generate clock with period {period_10MHz}ns"
        prev_time = current_sim_time


def test_miniALU():
    run(
        verilog_sources=glob.glob('slotMachine/hdl/*.sv'),
        toplevel="clock_divider",
        module="test_clock_divider",
        simulator="icarus",
        sim_build="slotMachine/sim_build/",
    )