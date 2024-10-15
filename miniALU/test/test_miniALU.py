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

        dut.op1.value = operand1
        dut.op2.value = operand2

        # operation = 0, sign = 0 -- addition
        dut.operation.value = 0
        dut.sign.value = 0

        await cocotb.triggers.Timer(10, units='ns') # delay

        exact = operand1 + operand2
        computed = dut.result.value.integer # read output (unsigned)
        assert exact == computed, f"Failed on the {i}th cycle. Got {computed}, expected {exact}"  # If any assertion fails, the test fails, and the string would be printed in console

        await cocotb.triggers.Timer(10, units='ns') # delay

        # operation = 0, sign = 1 -- subtraction
        dut.operation.value = 0
        dut.sign.value = 1

        await cocotb.triggers.Timer(10, units='ns') # delay

        exact = operand1 - operand2
        if exact < 0:
            exact += 2**20
        computed = dut.result.value.integer # read output (signed)
        assert exact == computed, f"Failed on the {i}th cycle. Got {computed}, expected {exact}"

        await cocotb.triggers.Timer(10, units='ns') # delay

        # operation = 1, sign = 0 -- left shift
        dut.operation.value = 1
        dut.sign.value = 0

        await cocotb.triggers.Timer(10, units='ns') # delay

        exact = operand1 << operand2
        computed = dut.result.value.integer # read output (unsigned)
        assert exact == computed, f"Failed on the {i}th cycle. Got {computed}, expected {exact}"  # If any assertion fails, the test fails, and the string would be printed in console

        await cocotb.triggers.Timer(10, units='ns') # delay

        # operation = 1, sign = 1 -- right shift
        dut.operation.value = 1
        dut.sign.value = 1

        await cocotb.triggers.Timer(10, units='ns') # delay

        exact = operand1 >> operand2
        computed = dut.result.value.integer # read output (unsigned)
        assert exact == computed, f"Failed on the {i}th cycle. Got {computed}, expected {exact}"  # If any assertion fails, the test fails, and the string would be printed in console

        await cocotb.triggers.Timer(10, units='ns') # delay


def test_miniALU():
    run(
        verilog_sources=glob.glob('miniALU/hdl/*.sv'),
        toplevel="miniALU",
        module="test_miniALU",
        simulator="icarus",
        sim_build="miniALU/sim_build/",
    )