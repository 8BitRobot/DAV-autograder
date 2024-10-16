<<<<<<< HEAD
`timescale 1ns/1ns		//	This line is necessary for the auto-grader. Feel free to remove when you assemble with the FPGA.
module clock_divider #( parameter MAX_SPEED = 50000000 ) (
	//	Inputs and outputs go here. 1-bit input "clk", 26-bit input "speed", 1-bit input "rst", and 1-bit output "clk_div". 
	//	Which inputs are wires, which are regs?
=======
`timescale 1ns/1ns		//	This line is necessary for Questa testbenches, and for the auto-grader.

//	Your other inputs are: 26-bit input "speed", 1-bit input "rst", and 1-bit reg output "clk_div". 
//	The distinction between reg and wire can be confusing; feel free to use "logic" instead.
module clock_divider #( parameter MAX_SPEED = 50000000 ) (
>>>>>>> c5c4f77e0bb92d1073b756cee391e9877bfcd0dd
	input clk					//	input clk signal
);

reg [25:0] count = 0;															//	count num pos edges
reg [25:0] NEW_DIVISOR = 0;
<<<<<<< HEAD
reg [25:0] DIVISOR = 0;															//	Max count before clk signal repeats

reg [1:0] rst_sr = 2'b00;

always @(posedge clk) begin													//	Activates on pos clk edge
//	You will be assigning a new value to your counter sequentially; what are the criteria to update the counter? When should it reset?
//	Your output will be either 0 or 1, depending on your counter value. If it's under half the maximum, output is 1, else 0, or vice versa.
//	Use a shift register to capture a button press!
end

always_comb begin
//	This block is for any variable that updates instantly based on the input values.
=======
reg [25:0] DIVISOR = 0;														//	Max count before clk signal repeats

reg [1:0] rst_sr = 2'b00;													//	Shift register to capture button press

always @(posedge clk) begin												//	Activates on pos clk edge
	//	Your counter should update on a clock edge. When should it reset? When should it increment?
	//	Your output signal will be 0 or 1, based on your counter.
	//	You will also need to assign your divisor value and reset shift-register value sequentially.
end

always_comb begin
	NEW_DIVISOR = MAX_SPEED / speed;		//	NEW_DIVISOR changes directly based on the input "speed." What does NEW_DIVISOR represent?
>>>>>>> c5c4f77e0bb92d1073b756cee391e9877bfcd0dd
end

endmodule