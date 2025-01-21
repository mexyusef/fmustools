# --% /np/react-antd/components/modules/Task/FormWrapper.js

form_wrapper = """
import React, { useEffect, useState } from 'react'
import FormProvider from './FormProvider'

const FormWrapper = ({
    onClose=()=>{},
    data_raw={},
    data_selected={},
}) => {
  return <>    
    <FormProvider 
      data_raw={data_raw} 
      onClose={onClose} />
  </>;
}

export default FormWrapper;
"""
