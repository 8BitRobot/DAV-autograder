import cocotb
import cocotb.triggers
import cocotb.clock
import random

from cocotb_test.simulator import run
import pytest
import glob

@cocotb.test()
async def clockDivider_tb(dut):
    ''' Assign random values to input, wait for a clock and verify output '''

    # 50 MHz clock period
    period_50MHz = 20

    clk_50MHz = cocotb.clock.Clock(dut.clk, period_50MHz, 'ns')
    print("hello")
    await cocotb.start(clk_50MHz.start())

    # 25 MHz clock period
    period_25MHz = 40
    dut.speed.value = 25000000
    dut.rst.value = 0

    prev_time = None
    
    for i in range(5):
        print("hello")
        await cocotb.triggers.RisingEdge(dut.clk_div)
        print(cocotb.utils.get_sim_time())
        # if prev_time != None:
        #     if prev_time + period_25MHz == 
        # compare the current simulation time to prev_time
        # reset prev_time
        # repeat
    
    
    '''
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
    '''


def test_miniALU():
    run(
        verilog_sources=glob.glob('slotMachine/hdl/*.sv'),
        toplevel="clock_divider",
        module="test_clock_divider",
        simulator="icarus",
        sim_build="slotMachine/sim_build/",
    )