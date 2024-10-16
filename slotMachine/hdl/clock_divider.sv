`timescale 1ns/1ns
module clock_divider #( parameter MAX_SPEED = 50000000 ) (
	//	Inputs and outputs go here. 1-bit input "clk", 26-bit input "speed", 1-bit input "rst", and 1-bit output "clk_div". 
	//	Which inputs are wires, which are regs?
	input clk					//	input clk signal
);

reg [25:0] count = 0;															//	count num pos edges
reg [25:0] NEW_DIVISOR = 0;
reg [25:0] DIVISOR = 0;															//	Max count before clk signal repeats

reg [1:0] rst_sr = 2'b00;

always @(posedge clk) begin													//	Activates on pos clk edge
//	You will be assigning a new value to your counter sequentially; what are the criteria to update the counter? When should it reset?
//	Your output will be either 0 or 1, depending on your counter value. If it's under half the maximum, output is 1, else 0, or vice versa.
//	Use a shift register to capture a button press!
end

always_comb begin
//	This block is for any variable that updates instantly based on the input values.
end

endmodule