
# The 1 and 0 of the Animatronic Hand 

This project relies on [pwm](https://en.wikipedia.org/wiki/Pulse-width_modulation "Pulse-width modulation")-driven servos controlled by [Adafruit RP2040 Feather](https://www.adafruit.com/product/4884) boards running CircuitPython attached to an [8-channel servo FeatherWing](https://www.adafruit.com/product/2928). 

## Physical Assembly

The Feather Board should be soldered using stacking headers for maximum reusability and flexibility. The FeatherWing should be soldered using stacking headers if available. The Feather Board should be attached to the FeatherWing using the stacking headers. The servos should be attached to the FeatherWing using the provided headers.

>[!NOTE]
>Soldering the Feather Board and FeatherWing directly together will make it difficult to reuse the Feather Board in other projects and thus highly not recommended as they do cost $20 per set.

## Feather Board Setup

To set up the Feather Board, you need to flash it with the latest version of CircuitPython available by following the instructions provided [here](https://learn.adafruit.com/adafruit-feather-rp2040-pico/circuitpython). Copy the `lib` folder in this repository to the Feather Board. Then, connect the Feather Board to your computer via USB and mount it as a drive. Replace the `code.py` file on the Feather Board with the `code.py` file in this repository. Finally, unmount and disconnect the Feather Board from the computer.

## FeatherWing Setup

(This section will be written if we discover that any additional setup is required for the FeatherWing.)

## Advanced Usage

### Using more than 8 servos

There is a potential that you would need to do so if your project demands more servos. In that case, you can use multiple FeatherWings to control more servos. You need to connect the FeatherWings to each other using the provided stacking headers. Finally, you need to connect the servos to the FeatherWings using 90-degree 4x3 headers. You must then modify the `code.py` file to configure it for more than one FeatherWing. Additionally, you must bridge the pads on the FeatherWings to select their I2C addresses. The default I2C address is 0x40. The other available addresses are 0x41, 0x42, and 0x43, etc, etc. You can find the pads on the back of the FeatherWing. The pads are labeled A0, A1, and up to A5. You need to bridge the pads to select the I2C address. For example, if you want to use the I2C address 0x41, you need to bridge the A0 pad. If you want to use the I2C address 0x42, you need to bridge the A1 pad. If you want to use the I2C address 0x43, you need to bridge the A0 and A1 pads. 
> [!NOTE]
> This is not necessary if you are only using one FeatherWing. In fact, if you are not using more than one FeatherWing, you should not bridge any of the pads.

## In Addendum

### How do the Feathers communicate with the FeatherWing?

The Feather Board communicates with the FeatherWing using [I2C](https://en.wikipedia.org/wiki/I%C2%B2C "I2C"). The Feather Board sends commands to the FeatherWing over the I2C bus to control the servos. This is why the FeatherWing has pads to bridge to select its I2C address. The Feather Board is configured to use the default I2C address of 0x40. If you need to use more than one FeatherWing, you need to change the I2C address of the FeatherWing by bridging the pads to one of the other addresses. You also need to change the I2C address of the Feather Board by modifying the `code.py` file.