# CRSFv2
This is an example CRSF code used for testing the interface between computer and TBS Crossfire TXv2. The implementation in Agilicious is much more efficient.

# CRSF Frame Structure
CRSF protocol consists of frames with the following structure: <br />
<Address Byte><Frame Length><Type><Payload><CRC> <br />

Address byte: For transmitting frames: 0xEE, for telemetry frames: 0xEA. <br />
Frame Length: Length of the type, payload and crc in bytes. It is 24 (0x18) for transmitting frames. <br />
Type: Type of the payload, 0x16 while transmitting, which corresponds to "RC channels packed". <br />
Payload: For transmitting frames, it is packed message from 16 channels. Each channel is 11 bits long, so it is 11*16 / 8 = 22 bytes. <br />
CRC: CRC8 to check if the message is corrupted with polynomial 0xD5. <br />

An example frame:<br />
b'\xee\x18\x16\xe1\xe3\xde\x09\xc7\xd7\x8a\x56\x80\x0f\x7c\xe0\x03\x1f\xf8\xc0\x07\x3e\xf0\x81\x0f\x7c\x36'<br />
