from xml.etree import ElementTree as Et
from io import BytesIO
from datetime import *


class Fields:
    def __init__(self, names, values):
        self.Names = names
        self.Values = values


class BaseXmlNode:
    def __init__(self, tag, value=None, fields=None, xmlms=None):
        if xmlms is None:
            self._xmlRoot = Et.Element(tag)
        else:
            self._xmlRoot = Et.Element(tag, xmlns=xmlms)
        if value is not None:
            self._xmlRoot.text = value
        if isinstance(fields, Fields):
            self._fields = dict.fromkeys(fields.Names)
            index = 0
            for vkey in fields.Names:
                # self._fields.setdefault(vkey, fields.Values[index] if index < len(fields.Values) else None)
                self._fields[vkey] = fields.Values[index] if index < len(fields.Values) else None
                index += 1
        else:
            self._fields = dict()

    def _addToTree(self, tag, value=None, root=None):
        if root is None:
            root = self._xmlRoot
        el = Et.SubElement(root, tag)
        el.text = value
        return el

    def append(self,item):
        if isinstance(item, BaseXmlNode):
            self._xmlRoot.append(item.getTreeRoot())
        else:
            raise ValueError('{item} wrong, use "baz" or "bar"'.format(item=repr(item)))

    def ToXmlStr(self):
        stream = BytesIO()
        for k in self._fields:
            self._addToTree(k, self._fields[k])
        tree = Et.ElementTree(self._xmlRoot)
        tree.write(stream, encoding='utf-8', xml_declaration=True)
        return stream.getvalue().decode("UTF-8")

    def GetTree(self):
        return Et.ElementTree(self._xmlRoot)

    def getTreeRoot(self):
        return self._xmlRoot


class Batch(BaseXmlNode):
    def __init__(self, ORIGINATOR="ORIGINATOR"):
        # names = ["ORIGINATOR", "SUPPRESS"]
        # values = ["ORIGINATOR", "y"]
        # fields = Fields(names, values)

        super().__init__("BATCH", fields=None, xmlms="urn:mclsoftware.co.uk:hunterII")
        self._ORIGINATOR = ORIGINATOR
        self._SUPPRESS = "y"
        self._SUBMISSIONS = []

    def ToXmlStr(self):
        self._createHeader()
        self._createSubmissions()
        return super().ToXmlStr()

    def _createHeader(self):
        # self._Header = Et.Element("HEADER")
        self._Header=BaseXmlNode("HEADER")
        keys=["COUNT", "ORIGINATOR", "SUPPRESS"]
        vals=[str(self.getCount()), self._ORIGINATOR, self._SUPPRESS]
        fields=dict(zip(keys,vals))
        self._Header._fields=fields

        for k in fields:
            self._addToTree(k, value=str(fields[k]), root=self._Header.getTreeRoot())

        self.append(self._Header)

    def getCount(self):
        return len(self._SUBMISSIONS)

    def _createSubmissions(self):
        subs = Et.Element("SUBMISSIONS")
        for item in self._SUBMISSIONS:
            subs.append(item.getTreeRoot())
        self._xmlRoot.append(subs)

    def Add(self, sub):
        self._SUBMISSIONS.append(sub)


class Submission(BaseXmlNode):
    def __init__(self):
        fieldsName = [
            "IDENTIFIER",
            "PRODUCT",
            "CLASSIFICATION",
            "DATE",
            "APP_DATE",
            "APPLICATION_VALUE",
            "INITIAL_PAYMENT",
            "GUARANTY",
            "PRODUCT_TYPE",
            "APP_CHANNEL",
            "SALPROJECT",
            "SECSALES",
            "APP_NUMBER",
            "REASON_CODE",
            "GDS_TYPE",
            "GDS_NAME",
            "GDS_CNT",
            "MG_PRICE",
            "TPA_DEF",
            "FPA_DEF",
            "CR_ACT"
        ]
        fieldsValues = [
            "ID-1011211411",
            "OD",
            "LM",
            str(datetime.now().date()),
            str(datetime.now().date())
        ]
        fields = Fields(fieldsName, fieldsValues)

        # super().__init__("SUBMISSION", fields=fields)

        super().__init__("SUBMISSION")

        self.IDENTIFIER = "ID-1011211411"
        self.PRODUCT = "OD"
        self.CLASSIFICATION = "LM"
        self.DATE = str(datetime.now().date())
        self.APP_DATE = str(datetime.now().date())

        # self.APPLICATION_VALUE
        # self.INITIAL_PAYMENT
        # self.GUARANTY
        # self.PRODUCT_TYPE
        # self.APP_CHANNEL
        # self.SALPROJECT
        # self.SECSALES
        # self.APP_NUMBER
        # self.REASON_CODE
        # self.GDS_TYPE
        # self.GDS_NAME
        # self.GDS_CNT
        # self.MG_PRICE
        # self.TPA_DEF
        # self.FPA_DEF
        # self.CR_ACT

    def getTreeRoot(self):
        self._addToTree("IDENTIFIER", self.IDENTIFIER)
        self._addToTree("PRODUCT", self.PRODUCT)
        self._addToTree("CLASSIFICATION", self.CLASSIFICATION)
        self._addToTree("DATE", self.DATE)
        self._addToTree("APP_DATE", self.APP_DATE)

        # self.append()

        return super().getTreeRoot()


class Applicant(BaseXmlNode):
    def __init__(self, Name, OchName, Surmane):
        super().__init__("MA")
        # < APP_TYPE > 5 < / APP_TYPE >
        self.PNAME = Name
        self.FNAME = OchName
        self.LNAME = Surmane
        self.DOB = str(datetime.now().date())
        self.DOB_OD = str(datetime.now().date())

        # self.PER_INN = None
        # self.PREV_FN = None
        # self.PREV_PN = None
        # self.PREV_LN = None
        # self.INC_TM = None
        # self.INC_DOC = None
        # self.INC_ADD = None
        # self.DIT_TYPE = None
        # self.INC_CALC = None
        # self.PER_INDEX = None
        # self.GENDER = None
        # self.EDUC_LVL = None
        # self.MARIT_ST = None
        # self.KIDS = None
        # self.AGRMNT_FLG = None
        # self.AGRMNT_STDT = None
        # self.AGRMNT_EXPDT = None
        # self.PD_COLL_PURP = None
        # self.WRK_LEN = None


def main():
    batch = Batch()
    sup = Submission()
    batch.Add(sup)
    print(batch.ToXmlStr())


if __name__ == '__main__':
    main()
