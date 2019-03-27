`include "vunit_defines.svh"

module module_a_tb;
  `TEST_SUITE begin

    `TEST_CASE("basic") begin
      $display("Hello world basic");
    end

    `TEST_CASE("advanced") begin
      $display("Hello world advanced");
    end

  end
endmodule
