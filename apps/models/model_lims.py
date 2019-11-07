# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Index, Integer, String, text
from apps.databases.db_lims import db_lims


Base = db_lims.Model
metadata = Base.metadata


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

Base.to_dict = to_dict
Base.__bind_key__ = 'db_lims'


class Calendar(Base):
    __tablename__ = 'calendar'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, server_default=text("''"))
    date = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    week = Column(Integer, nullable=False, server_default=text("'0'"))
    status_holiday = Column(Integer, nullable=False, server_default=text("'0'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True, server_default=text("''"))
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
        Index('source_id', 'source_id', 'type_source'),
    )

    id = Column(Integer, primary_key=True)
    operation_uid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    type_operation = Column(Integer, nullable=False, server_default=text("'0'"))
    result = Column(Integer, nullable=False, server_default=text("'0'"))
    type_source = Column(Integer, nullable=False, server_default=text("'0'"))
    source_id = Column(Integer, nullable=False, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class Protocol(Base):
    __tablename__ = 'protocol'

    id = Column(Integer, primary_key=True)
    code = Column(String(100), nullable=False, server_default=text("''"))
    name = Column(String(100), nullable=False, server_default=text("''"))
    item_name = Column(String(100), nullable=False, server_default=text("''"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class ProtocolAndMethodRelation(Base):
    __tablename__ = 'protocol_and_method_relation'

    id = Column(Integer, primary_key=True)
    protocol_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    test_method_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    name = Column(String(100), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CompanyContact(Base):
    __tablename__ = 'company_contact'

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


class ReportInfo(Base):
    __tablename__ = 'report_info'

    id = Column(Integer, primary_key=True)
    report_no = Column(String(100), nullable=False, server_default=text("''"))
    receiver_uid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    submitter_cid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    submitter_uid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    be_inspected_entity_cid = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    inspection_type = Column(Integer, nullable=False, server_default=text("'0'"))
    test_type = Column(Integer, nullable=False, server_default=text("'0'"))
    sample_grade_id = Column(Integer, nullable=False, server_default=text("'0'"))
    sample_quantity = Column(String(100), nullable=False, server_default=text("''"))
    sample_description = Column(String(256), nullable=False, server_default=text("''"))
    style_number = Column(String(100), nullable=False, server_default=text("''"))
    sku_number = Column(String(100), nullable=False, server_default=text("''"))
    sample_brand = Column(String(100), nullable=False, server_default=text("''"))
    period = Column(Integer, nullable=False, server_default=text("'0'"))
    req_date = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    arr_date = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class ReportSample(Base):
    __tablename__ = 'report_sample'

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


class ReportSubSample(Base):
    __tablename__ = 'report_sub_sample'

    id = Column(Integer, primary_key=True)
    code = Column(String(100), nullable=False, server_default=text("''"))
    name = Column(String(100), nullable=False, server_default=text("''"))
    specimen_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    report_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_allocate = Column(Integer, nullable=False, server_default=text("'0'"))
    allocate_time = Column(DateTime)
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SampleGrade(Base):
    __tablename__ = 'sample_grade'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, server_default=text("''"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SampleTestedItems(Base):
    __tablename__ = 'sample_tested_items'

    id = Column(Integer, primary_key=True)
    code = Column(String(100), nullable=False, server_default=text("''"))
    name = Column(String(100), nullable=False, server_default=text("''"))
    sub_sample_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    protocol_id = Column(Integer, nullable=False, server_default=text("'0'"))
    test_method_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    report_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TestMethod(Base):
    __tablename__ = 'test_method'

    id = Column(Integer, primary_key=True)
    code = Column(String(100), nullable=False, unique=True, server_default=text("''"))
    name = Column(String(100), nullable=False, server_default=text("''"))
    condition = Column(String(100), nullable=False, server_default=text("''"))
    note = Column(String(256), nullable=False, server_default=text("''"))
    status_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    delete_time = Column(DateTime)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class TestProperty(Base):
    __tablename__ = 'test_property'

    id = Column(Integer, primary_key=True)
    test_method_id = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    property = Column(String(100), nullable=False, server_default=text("''"))
    sort_code = Column(Integer, nullable=False, server_default=text("'0'"))
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
