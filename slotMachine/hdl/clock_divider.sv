`timescale 1ns/1ns
module clock_divider #( parameter MAX_SPEED = 50000000 ) (
	input clk,					//	input clk signal
	input [25:0] speed,
	input rst,
	output reg clk_div		//	output clk signal
);

	assign clk_div = 1;

endmodule