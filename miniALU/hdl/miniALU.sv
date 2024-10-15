`timescale 1ns/1ns
module miniALU (
    // TODO: define your input and output ports
    input logic [3:0] op1,
    input logic [3:0] op2, 
    input logic operation,
    input logic sign, 
    output logic [19:0] result
    );

    assign result = 'd1;
endmodule