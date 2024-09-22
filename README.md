# MAC Changer Project

**```ifconfig```** code is used to get action too, not just to get ip and mac adress ets.

**```ifconfig eth0 down```**

This code cuts eth0 connection.
eth0 is first ethernet interface. Maybe we can say this is first ethernet motherboard. 
Ordinairly mac adress has writted in etherent card by producer firm. 
We said that find which interface eth0 that will be configurated. Than deactive the ethernet interface with down code.

**```ifconfig eth0 hw ether m:ma:cA:dd:re:ss```**

This code changes mac adress in eth0. 
We said that find which interface eth0 that will be configurated. Than I m gonna make some changes on hardware(hw) that is physically part of computer. Find ether adress and I'm gonna change the adress as m:ma:cA:dd:re:ss.

**```ifconfig eth0 up```**

We said that find which interface eth0 that will be configurated. Than active the ethernet interface with up code.

---

While we use **```optparse```** library and write options in the ```optparse object``` we get a tuple object.
tuple-type objects seems dictionary-type objects but tuple-type objects are **```immutable```** types. You can read but you can not change any item of tuple. 
When we attact any computer we can get tuple type data. We can not change the data.

Ordinarily we use ```thelist = ["a", 'd', 1, 5]``` shape, when we define a list but
tuple objects defines like:

**```my_tuple = ('a', "s", 1, 3)```**

In this code we are entering some arguments as response of selections like ```-i --interface```. The tuple object that we got includes different objects like selections, our string-value couples like ```"mac":"m:ma:cA:dd:re:ss"```, help strings. 
Actually this tuple holds added options selections.

**```(inputs, args) = parse_obj.parse_args()```**

When we write this code, code analyses as couple of options - users inputs to inputs and if we entered extra arguments without options args holds that. If we enter this code
**```python cmac.py -i eth0 -m 00:11:22:33:44:55 extra_argument```** on console **```args```** holds **```'extra_arguement'```**

**```subprocess.call(["ifconfig", interface , "down"])```**
we are calling this code to realize UNIX functions one by one. interface is a variable what we write for this.
