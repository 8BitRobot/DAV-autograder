import cocotb
import cocotb.triggers
import random

from cocotb_test.simulator import run
import pytest
import glob

@cocotb.test()
async def miniALU_tb(dut):
    ''' Assign random values to input, wait for a clock and verify output '''
    for i in range(50): # 50 experiments
        operand1 = random.randint(0, 15) # generate randomized input
        operand2 = random.randint(0, 15)

        dut.operand1.value = operand1
        dut.operand2.value = operand2
        dut.select.value = 0

        await cocotb.triggers.Timer(10, units='ns') # delay

        exact = operand1 << operand2
        computed = dut.result.value.integer # read output (unsigned)
        assert exact == computed, f"Failed on the {i}th cycle. Got {computed}, expected {exact}"  # If any assertion fails, the test fails, and the string would be printed in console

        await cocotb.triggers.Timer(10, units='ns') # delay

        dut.select.value = 1

        await cocotb.triggers.Timer(10, units='ns') # delay

        exact = operand1 + operand2
        computed = dut.result.value.integer # read output (signed)
        assert exact == computed, f"Failed on the {i}th cycle. Got {computed}, expected {exact}"

        print(f"Driven value: {exact} \t received value: {computed}") 


def test_miniALU():
    run(
        verilog_sources=glob.glob('miniALU/hdl/*.sv'),
        toplevel="miniALU",
        module="test_miniALU",
        simulator="icarus",
        sim_build="miniALU/sim_build/",
    )