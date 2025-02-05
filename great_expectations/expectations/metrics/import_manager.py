"""
This file manages common global-level imports for which we want to centralize error handling
"""
import logging

logger = logging.getLogger(__name__)
sa_import_warning_required = False
spark_import_warning_required = False

try:
    import sqlalchemy as sa  # noqa: TID251
except ImportError:
    logger.debug("No SqlAlchemy module available.")
    sa = None

try:
    from sqlalchemy.engine import Engine as sqlalchemy_engine_Engine  # noqa: TID251
    from sqlalchemy.engine import Row as sqlalchemy_engine_Row  # noqa: TID251
    from sqlalchemy.engine import reflection  # noqa: TID251
except ImportError:
    logger.debug("No SqlAlchemy.engine module available.")
    reflection = None
    sqlalchemy_engine_Engine = None
    sqlalchemy_engine_Row = None

try:
    import sqlalchemy.func.count as sa_func_count  # noqa: TID251
except ImportError:
    logger.debug("No SqlAlchemy.func module available.")
    sa_func_count = None

try:
    import sqlalchemy.sql.expression.ColumnClause as sa_sql_expression_ColumnClause  # noqa: TID251
    import sqlalchemy.sql.expression.Select as sa_sql_expression_Select  # noqa: TID251
    import sqlalchemy.sql.expression.Selectable as sa_sql_expression_Selectable  # noqa: TID251
except ImportError:
    logger.debug("No SqlAlchemy.sql.expression module available.")
    sa_sql_expression_ColumnClause = None
    sa_sql_expression_Select = None
    sa_sql_expression_Selectable = None

try:
    from sqlalchemy.sql.elements import quoted_name  # noqa: TID251
except ImportError:
    logger.debug("No SqlAlchemy.sql.elements module available.")
    quoted_name = None

try:
    import pyspark.sql.functions as F
    import pyspark.sql.types as sparktypes
except ImportError:
    logger.debug("No spark functions module available.")
    sparktypes = None  # type: ignore[assignment]
    F = None  # type: ignore[assignment]

try:
    from pyspark.ml.feature import Bucketizer
except ImportError:
    logger.debug("No spark Bucketizer available.")
    Bucketizer = None  # type: ignore[assignment,misc]

try:
    from pyspark.sql import Window
except ImportError:
    logger.debug("No spark Window function available.")
    Window = None  # type: ignore[assignment,misc]

try:
    from pyspark.sql import Column as pyspark_sql_Column
    from pyspark.sql import DataFrame as pyspark_sql_DataFrame
    from pyspark.sql import Row as pyspark_sql_Row
    from pyspark.sql import SparkSession as pyspark_sql_SparkSession
    from pyspark.sql import SQLContext
except ImportError:
    logger.debug("No spark SQLContext available.")
    SQLContext = None  # type: ignore[assignment,misc]
    pyspark_sql_Column = None  # type: ignore[assignment,misc]
    pyspark_sql_DataFrame = None  # type: ignore[assignment,misc]
    pyspark_sql_Row = None  # type: ignore[assignment,misc]
    pyspark_sql_SparkSession = None  # type: ignore[assignment,misc]
