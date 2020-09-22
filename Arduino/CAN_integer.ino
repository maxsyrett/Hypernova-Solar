extern "C"{
  #include <conv.h>
}

#include <mcp_can.h>
#include <mcp_can_dfs.h>

MCP_CAN CAN0(10);

void setup() {
  CAN0.begin(MCP_ANY, CAN_500KBPS, MCP_8MHZ);
  CAN0.setMode(MCP_NORMAL);
}
byte *data;
void loop() {
  for(int i = 0;i < 256;i++) {
    data = intToByteArr(i);
    CAN0.sendMsgBuf(0x104, 0, int_len, data);
    delay(1000);
  }
  delay(1000);
}
