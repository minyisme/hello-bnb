""" Phillips Hue Modules"""
# python libs

# third party libs
import pprint
import requests
import json
import urllib
import urllib2

# my libs


class HueControls(object):
    """ Controls for Hue """

    def __init__(self):
        """ Initialize HueControls Class """
        
        self.username = None


    def get_authorize(self):
        """ Sets up authorize username to communicate with Hue API """

        # username is set up using devicetype to the name of the Hue bridge
        payload = {"devicetype":"Huedev028"}

        # make post request to Hue to request authorization to device
        r = requests.post("http://10.10.30.175/api", data=json.dumps(payload))
       
        # Hue json response to python
        resp = r.json()

        # variable to hold hue object(dictionary)
        hue_r = resp[0]

        print "hue r", hue_r
        # if authorize user successfully created, store on object
        # in order for object to communicate with Hue to control lights.
        # if authorization fails, return error.
        if hue_r.get('success'):
            self.username = hue_r.get('success').get('username')
            return "success: extracted username {}".format(self.username)
        elif hue_r.get('error'):
            return "error: {}".format(hue_r.get('error').get('description'))
        else:
            return "error: Could not parse valid response from hue\n{}".format(hue_r)

    def get_lights(self):
        """ Returns a list of all lights controlled by Hue Bridge """

        lights = requests.get("http://10.10.30.175/api/" + self.username + "/lights")
        
        # should I loop over each light and create a seperate object class
        # with a num attribute and a light toggle method?
        return lights.json()

# class Light(HueControls):
    # """ Creates a single light object for each bridge light to control """

    # def __init__(self, num):
    #     self.num = num
        
# consider seperating this to a new class
    def light_on(self, num): 
        """ Turns on a light based on the light number provided """



        light_state = requests.get("http://10.10.30.175/api/" + self.username + "/lights/" + str(num) + "/state")
        # make put request to update light state to on

        resp = light.json()

        # if light is off, put request to turn it on,
        # otherwise put request to turn it off
        if resp.state == "off":
             # set light state to on
            payload = {"on": True}
            light = requests.put("http://10.10.30.175/api/" + self.username + "/lights/" + str(num) + "/state", data=json.dumps(payload))
        else:
            # set light state to on
            payload = {"on": False}
            light = requests.put("http://10.10.30.175/api/" + self.username + "/lights/" + str(num) + "/state", data=json.dumps(payload))

        # resp = light.json()
        
        return resp

    def light_off(self, num):
        """ Turns off a light based on the light number provided """

        # set light state to off
        payload = {"on": False}

        # make put request to update light state to off
        light = requests.put("http://10.10.30.175/api/" + self.username + "/lights/" + str(num) + "/state", data=json.dumps(payload))
        resp = light.json()
        
        return resp



if __name__ == "__main__":
    pp = pprint.PrettyPrinter()
    hue = HueControls()
    hue.get_authorize()
    