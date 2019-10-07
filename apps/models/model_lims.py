# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Index, Integer, String, text
from apps.databases.db_lims import db_lims


Base = db_lims.Model
metadata = Base.metadata


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict
Base.__bind_key__ = 'db_lims'


class Applicant(Base):
    __tablename__ = 'applicant'

    id = Column(Integer, primary_key=True)
    code = Column(String(100), nullable=False, server_default=text("''"))
    receiver_uid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    applicant_cid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    applicant_uid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    detection_cid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    type_detection = Column(Integer, nullable=False, server_default=text("'0'"))
    type_test = Column(Integer, nullable=False, server_default=text("'0'"))
    grade_id = Column(Integer, nullable=False, server_default=text("'0'"))
    summary = Column(String(100), nullable=False, server_default=text("''"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    style = Column(String(100), nullable=False, server_default=text("''"))
    sku = Column(String(100), nullable=False, server_default=text("''"))
    brand = Column(String(100), nullable=False, server_default=text("''"))
    period = Column(Integer, nullable=False, server_default=text("'0'"))
    req_date = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    arr_date = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, server_default=text("''"))
    address = Column(String(100), nullable=False, server_default=text("''"))
    site = Column(String(100), nullable=False, server_default=text("''"))
    tel = Column(String(100), nullable=False, server_default=text("''"))
    fax = Column(String(100), nullable=False, server_default=text("''"))
    email = Column(String(100), nullable=False, server_default=text("''"))
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_locked = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    locked_time = Column(DateTime)
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    cid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    name = Column(String(20), nullable=False, server_default=text("''"))
    salutation = Column(String(20), nullable=False, server_default=text("''"))
    mobile = Column(String(20), nullable=False, server_default=text("''"))
    email = Column(String(60), nullable=False, server_default=text("''"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_default = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, server_default=text("''"))
    lab_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Detection(Base):
    __tablename__ = 'detection'

    id = Column(Integer, primary_key=True)
    code = Column(String(100), nullable=False, server_default=text("''"))
    name = Column(String(100), nullable=False, server_default=text("''"))
    specimen_item_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    manner_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    applicant_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Grade(Base):
    __tablename__ = 'grade'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, server_default=text("''"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Holiday(Base):
    __tablename__ = 'holiday'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, server_default=text("''"))
    date = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Laboratory(Base):
    __tablename__ = 'laboratory'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, server_default=text("''"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class LogOperation(Base):
    __tablename__ = 'log_operation'
    __table_args__ = (
        Index('source_id', 'source_id', 'source_type'),
    )

    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, nullable=False, server_default=text("'0'"))
    source_type = Column(Integer, nullable=False, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Manner(Base):
    __tablename__ = 'manner'

    id = Column(Integer, primary_key=True)
    code = Column(String(100), nullable=False, server_default=text("''"))
    name = Column(String(100), nullable=False, server_default=text("''"))
    standard_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Specimen(Base):
    __tablename__ = 'specimen'

    id = Column(Integer, primary_key=True)
    code = Column(String(100), nullable=False, server_default=text("''"))
    name = Column(String(100), nullable=False, server_default=text("''"))
    applicant_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    grade_id = Column(Integer, nullable=False, server_default=text("'0'"))
    style = Column(String(100), nullable=False, server_default=text("''"))
    sku = Column(String(100), nullable=False, server_default=text("''"))
    brand = Column(String(100), nullable=False, server_default=text("''"))
    period = Column(Integer, nullable=False, server_default=text("'0'"))
    req_date = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    arr_date = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SpecimenItem(Base):
    __tablename__ = 'specimen_item'

    id = Column(Integer, primary_key=True)
    code = Column(String(100), nullable=False, server_default=text("''"))
    name = Column(String(100), nullable=False, server_default=text("''"))
    specimen_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    applicant_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Standard(Base):
    __tablename__ = 'standard'

    id = Column(Integer, primary_key=True)
    code = Column(String(100), nullable=False, server_default=text("''"))
    name = Column(String(100), nullable=False, server_default=text("''"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        Index('name', 'name', 'lab_id', 'dep_id', unique=True),
        Index('lab_id', 'lab_id', 'dep_id')
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(20, u'utf8mb4_bin'), nullable=False, server_default=text("''"))
    salutation = Column(String(20), nullable=False, server_default=text("''"))
    mobile = Column(String(20), nullable=False, server_default=text("''"))
    tel = Column(String(20), nullable=False, server_default=text("''"))
    fax = Column(String(20), nullable=False, server_default=text("''"))
    email = Column(String(60), nullable=False, server_default=text("''"))
    role_id = Column(Integer, nullable=False, server_default=text("'0'"))
    lab_id = Column(Integer, nullable=False, server_default=text("'0'"))
    dep_id = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class UserAuth(Base):
    __tablename__ = 'user_auth'
    __table_args__ = (
        Index('type_auth', 'type_auth', 'auth_key', unique=True),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    type_auth = Column(Integer, nullable=False, server_default=text("'0'"))
    auth_key = Column(String(60, u'utf8mb4_bin'), nullable=False, server_default=text("''"))
    auth_secret = Column(String(60, u'utf8mb4_bin'), nullable=False, server_default=text("''"))
    status_verify = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    verify_time = Column(DateTime)
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
