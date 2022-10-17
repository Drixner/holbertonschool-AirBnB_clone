#!/usr/bin/python3
#!/usr/bin/python3
"""
Unittest for base module
"""
import io
import unittest
import os
import models
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_BaseModel(unittest.TestCase):
    """ Test for
    Base_Model Class """

    def setUp(self):
        """set up the
        test for testing bae models"""
        FileStorage._FileStorage__file_path = "file.json"

    def test_noarg(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_None(self):
        Bmodel = BaseModel(None)
        self.assertNotIn(None, Bmodel.__dict__.values())

    def test_publicid(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_public_createat(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_public_updateat(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_all_storage_obj(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_all_str(self):
        date_time = datetime.today()
        date_repr = repr(date_time)
        Bmodel = BaseModel()
        Bmodel.id = "456789123"
        Bmodel.created_at = Bmodel.updated_at = date_time
        Bmodel_str = Bmodel.__str__()
        self.assertIn("[BaseModel] (456789123)", Bmodel_str)
        self.assertIn("'id': '456789123'", Bmodel_str)
        self.assertIn("'created_at': " + date_repr, Bmodel_str)
        self.assertIn("'updated_at': " + date_repr, Bmodel_str)

    def test_two_models(self):
        Bmodel1 = BaseModel()
        Bmodel2 = BaseModel()
        self.assertNotEqual(Bmodel1.id, Bmodel2.id)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        date_time = datetime.today()
        date_iso = date_time.isoformat()
        Bmodel = BaseModel(id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(Bmodel.id, "123")
        self.assertEqual(Bmodel.created_at, date_time)
        self.assertEqual(Bmodel.updated_at, date_time)


class Test_save(unittest.TestCase):

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("temp", "file.json")
        except IOError:
            pass

    def testsave(self):
        Bmodel = BaseModel()
        Update_at = Bmodel.updated_at
        Bmodel.save()
        self.assertLess(Update_at, Bmodel.updated_at)

    def testsave_arg(self):
        Bmodel = BaseModel()
        with self.assertRaises(TypeError):
            Bmodel.save(None)

    def testsave_update(self):
        Bmodel = BaseModel()
        Bmodel.save()
        Bmodelid = "BaseModel." + Bmodel.id
        with open("file.json", "r") as f:
            self.assertIn(Bmodelid, f.read())

    def testmulsave(self):
        Bmodel = BaseModel()
        f_updated_at = Bmodel.updated_at
        Bmodel.save()
        s_updated_at = Bmodel.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        Bmodel.save()
        self.assertLess(s_updated_at, Bmodel.updated_at)


class Test_to_dict(unittest.TestCase):

    def testto_dict(self):
        dt = datetime.today()
        Bmodel = BaseModel()
        Bmodel.id = "123"
        Bmodel.created_at = Bmodel.updated_at = dt
        todict = {
            "id": "123",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
            "__class__": "BaseModel"
        }
        self.assertDictEqual(Bmodel.to_dict(), todict)

    def testtype(self):
        Bmodel = BaseModel()
        self.assertTrue(dict, type(Bmodel.to_dict()))

    def testto_dict_arg(self):
        Bmodel = BaseModel()
        with self.assertRaises(TypeError):
            Bmodel.to_dict(None)

    def testto_dict_arg(self):
        Bmodel = BaseModel()
        self.assertNotEqual(Bmodel.to_dict(), Bmodel.__dict__)

    def testto_dict_created_at(self):
        Bmodel = BaseModel()
        DBmodel = Bmodel.to_dict()
        self.assertEqual(str, type(DBmodel["created_at"]))

    def testto_dict_updated_at(self):
        Bmodel = BaseModel()
        DBmodel = Bmodel.to_dict()
        self.assertEqual(str, type(DBmodel["updated_at"]))

    def testattr(self):
        Bmodel = BaseModel()
        Bmodel_nm = 'Holberton'
        Bmodel_num = 89
        self.assertNotIn('name', Bmodel.to_dict())
        self.assertNotIn('my_number', Bmodel.to_dict())

    def testmuldict(self):
        Bmodel = BaseModel()
        with self.assertRaises(TypeError):
            Bmodel.to_dict(None)


if __name__ == "__main__":
    unittest.main()
