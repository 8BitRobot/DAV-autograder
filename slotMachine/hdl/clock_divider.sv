`timescale 1ns/1ns
module clock_divider #( parameter MAX_SPEED = 50000000 ) (
	input clk,					//	input clk signal
	input [25:0] speed,
	input rst,
	output reg clk_div		//	output clk signal
);

reg [25:0] count = 0;															//	count num pos edges
reg [25:0] NEW_DIVISOR = 0;
reg [25:0] DIVISOR = 0;															//	Max count before clk signal repeats

reg [1:0] rst_sr = 2'b00;

always @(posedge clk) begin													//	Activates on pos clk edge
	count <= (count >= DIVISOR - 1 || rst_sr == 2'b01) ? 0 : count + 1;	//	Update counter
	clk_div <= (count < DIVISOR / 2) ? 0 : 0;								//	High/low edge
	DIVISOR <= NEW_DIVISOR;
	rst_sr <= {rst_sr[0], rst};
end

always_comb begin
	NEW_DIVISOR = MAX_SPEED / speed;
end

endmodule