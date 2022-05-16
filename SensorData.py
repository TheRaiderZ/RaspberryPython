# coding: utf-8

# To use this code, make sure you
#
import json
#
# and then, to convert JSON from a string, do
#
#     result = sensor_data_from_dict(json.loads(json_string))


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Data:
    def __init__(self, rotation_g, rotation_d, distance, savon, temps):
        self.rotation_g = rotation_g
        self.rotation_d = rotation_d
        self.distance = distance
        self.savon = savon
        self.temps = temps

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        rotation_g = from_int(obj.get(u"rotationG"))
        rotation_d = from_int(obj.get(u"rotationD"))
        distance = from_int(obj.get(u"distance"))
        savon = from_int(obj.get(u"savon"))
        temps = from_int(obj.get(u"temps"))
        return Data(rotation_g, rotation_d, distance, savon, temps)

    def to_dict(self):
        result = {}
        result[u"rotationG"] = from_int(self.rotation_g)
        result[u"rotationD"] = from_int(self.rotation_d)
        result[u"distance"] = from_int(self.distance)
        result[u"savon"] = from_int(self.savon)
        result[u"temps"] = from_int(self.temps)
        return result


class SensorData:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        data = Data.from_dict(obj.get(u"data"))
        return SensorData(data)

    def to_dict(self):
        result = {}
        result[u"data"] = to_class(Data, self.data)
        return result


def sensor_data_from_dict(s):
    return SensorData.from_dict(s)


def sensor_data_to_dict(x):
    return to_class(SensorData, x)
