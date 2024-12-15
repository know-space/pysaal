from enum import Enum

from pysaal.lib._sgp4_prop import (
    GP_ERR_ANEGATIVE,
    GP_ERR_ATOOLARGE,
    GP_ERR_BADFK,
    GP_ERR_E2TOOLARGE,
    GP_ERR_EHYPERPOLIC,
    GP_ERR_ENEGATIVE,
    GP_ERR_MATOOLARGE,
    GP_ERR_NONE,
)


class SGP4ErrorCode(Enum):

    NONE = GP_ERR_NONE
    BAD_FK_MODEL = GP_ERR_BADFK
    NEGATIVE_A = GP_ERR_ANEGATIVE
    LARGE_A = GP_ERR_ATOOLARGE
    HYPERBOLIC_E = GP_ERR_EHYPERPOLIC
    NEGATIVE_E = GP_ERR_ENEGATIVE
    LARGE_MA = GP_ERR_MATOOLARGE
    LARGE_E2 = GP_ERR_E2TOOLARGE