module miniALU (
    // TODO: define your input and output ports
    input logic [3:0] op1,
    input logic [3:0] op2, 
    input logic operation,
    input logic sign, 
    output logic [19:0] result
    );

    // The following block contains the logic of your combinational circuit
    always_comb begin
        // TODO: write the logic for your miniALU here
        if (~operation & ~sign) begin
            result <= op1 + op2;
        end else if (~operation & sign) begin
            result <= op1 - op2;
        end else if (operation & ~sign) begin
            result <= op1 << op2;
        end else begin
            result <= op1 >> op2;
        end
    end
endmodule