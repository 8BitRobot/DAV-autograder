`timescale 1ns/1ns		//	This line is necessary for Questa testbenches, and for the auto-grader.

//	Your other inputs are: 26-bit input "speed", 1-bit input "rst", and 1-bit reg output "clk_div". 
//	The distinction between reg and wire can be confusing; feel free to use "logic" instead.
module clock_divider #( parameter MAX_SPEED = 50000000 ) (
	input clk					//	input clk signal
);

reg [25:0] count = 0;															//	count num pos edges
reg [25:0] NEW_DIVISOR = 0;
reg [25:0] DIVISOR = 0;														//	Max count before clk signal repeats

reg [1:0] rst_sr = 2'b00;													//	Shift register to capture button press

always @(posedge clk) begin												//	Activates on pos clk edge
	//	Your counter should update on a clock edge. When should it reset? When should it increment?
	//	Your output signal will be 0 or 1, based on your counter.
	//	You will also need to assign your divisor value and reset shift-register value sequentially.
end

always_comb begin
	NEW_DIVISOR = MAX_SPEED / speed;		//	NEW_DIVISOR changes directly based on the input "speed." What does NEW_DIVISOR represent?
end

endmodule