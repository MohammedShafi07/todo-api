#    Copyright (c) 2020-2021. This file and the project containing this file is the sole property of
#    Slashbeyond Interactive Pvt Ltd.
#    NOTICE:  All information contained herein is, and remains the property of Slashbeyond Interactive Pvt Ltd.
#    The intellectual and technical concepts contained herein are proprietary to Slashbeyond Interactive Pvt Ltd and
#    may/may not be covered by Indian and Foreign Patents, patents in process, and are protected by trade secret
#    or copyright law. Dissemination of this information or reproduction of this material is strictly forbidden
#    unless prior written permission is obtained from Slashbeyond Interactive Pvt Ltd.  Access to the source code
#    contained herein is hereby forbidden to anyone except current Slashbeyond Interactive Pvt Ltd employees, managers
#    or contractors who have executed Confidentiality and Non-disclosure agreements explicitly covering such access.
#    The copyright notice above does not evidence any actual or intended publication or disclosure  of  this source
#    code, which includes information that is confidential and/or proprietary, and is a trade secret, of
#    Slashbeyond Interactive Pvt Ltd.   ANY REPRODUCTION, MODIFICATION, DISTRIBUTION, PUBLIC  PERFORMANCE, OR PUBLIC
#    DISPLAY OF OR THROUGH USE OF THIS SOURCE CODE WITHOUT THE EXPRESS WRITTEN CONSENT OF Slashbeyond Interactive Pvt
#    Ltd IS STRICTLY PROHIBITED, AND IN VIOLATION OF APPLICABLE LAWS AND INTERNATIONAL TREATIES. THE RECEIPT OR
#    POSSESSION OF THIS SOURCE CODE AND/OR RELATED INFORMATION DOES NOT CONVEY OR IMPLY ANY RIGHTS TO REPRODUCE,
#    DISCLOSE OR DISTRIBUTE  ITS CONTENTS, OR TO MANUFACTURE, USE, OR SELL ANYTHING THAT IT  MAY DESCRIBE, IN WHOLE
#    OR IN PART.

from pydantic import ValidationError
from src.common import errors


def map_models(destination_model_type, source_model, exclude_fields=None):
    """
    Map pydantic model(source) to another model(destination).
    Raise pydantic validation error in case of failure.
    This universal function will try mapping 2 pydantic models and catch the error if it fails.
    The error is returned to the caller.

    - ***exclude_fields*** : (default None) dict of fields to be excluded from mapping
    """
    try:
        if exclude_fields is not None:
            model = destination_model_type(**source_model.dict(exclude=exclude_fields))
        else:
            model = destination_model_type(**source_model.dict())
    except ValidationError as e:
        return None, errors.parse(e)

    return model, None
