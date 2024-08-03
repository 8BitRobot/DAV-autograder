`timescale 1ns/1ns

module miniALU(
    input  logic [3:0]  operand1,
    input  logic [3:0]  operand2,
    input  logic        select,
    output logic [19:0] result
);
    assign result = 1;
endmodule