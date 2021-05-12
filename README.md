# ikea-smartlight
python framework for controlling the Ikea smart lights (tradfri)

### requirements

To use this collection of small scripts for interacting with the Ikea
smart home "gateway" you will need [libcoap](https://libcoap.net)
version >= 4.2 with DTLS support.

The framework also requires `tqdm` for showing progressbars, you could strip it from the sourcecode or install the module for python: `pip install pip --upgrade && pip install tqdm`.

### libcoap usage
```bash
# getting tradfri information
./coap-client -m get -u "Client_identity" -k "<key>" "coaps://<hup>:5684/15001"
# getting tradfri lightbulb status
./coap-client -m get -u "Client_identity" -k "<key>" "coaps://<hup>:5684/15001/65537"

# turn on tradfri lightbulb
./coap-client -m put -u "Client_identity" -k "<key>" -e '{ "3311" : [{ "5850" : 1 ]} }' "coaps://<hup>:5684/15001/65537"
# turn off tradfri lightbulb
./coap-client -m put -u "Client_identity" -k "<key>" -e '{ "3311" : [{ "5850" : 0 ]} }' "coaps://<hup>:5684/15001/65537"
```

### output
```
./tradfri-status.py
[ ] tradfri: requireing all tradfri devices, please wait ...
tradfri lightbulbs: 100%|█████████████████████████████████████████████████████████| 8/8 [00:00<00:00, 10.93 lightbulb/s]
tradfri groups: 100%|█████████████████████████████████████████████████████████████████| 4/4 [00:00<00:00, 10.50 group/s]
[+] tradfri: device information gathered
===========================================================

bulbid 65537, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65538, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65539, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65540, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65542, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65541, name: TRADFRI bulb E27, bightness: 1, state: off
bulbid 65544, name: TRADFRI bulb E27, bightness: 254, state: off


groupid: 137274, name: hal beneden, state: off
groupid: 183216, name: slaapkamer, state: off
groupid: 140387, name: woonkamer, state: off
groupid: 186970, name: hal boven, state: off
```

### todo
- [X] add change state (power on/off lightbulb)
- [X] add dimmer value (dimm lightbulb)
- [X] add change state group (power on/off groups)
- [X] add dimmer value group (dimm group)
- [X] add color temperature lightbulb (switch to cold, normal or warm)

### licensing and credits
ikea-smartlight is licensed under the GPLv3:
```
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

For the full license, see the LICENSE file.
```
