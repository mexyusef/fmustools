import axios from 'axios'
import config from '../config'
import {
  __TABLENAME_UPPER___CREATE_REQUEST,
  __TABLENAME_UPPER___CREATE_SUCCESS,
  __TABLENAME_UPPER___CREATE_FAIL,
  __TABLENAME_UPPER___CREATE_RESET,

  __TABLENAME_UPPER___LIST_REQUEST,
  __TABLENAME_UPPER___LIST_SUCCESS,
  __TABLENAME_UPPER___LIST_FAIL,
  __TABLENAME_UPPER___LIST_RESET,

  __TABLENAME_UPPER___DETAIL_REQUEST,
  __TABLENAME_UPPER___DETAIL_SUCCESS,
  __TABLENAME_UPPER___DETAIL_FAIL,
  __TABLENAME_UPPER___DETAIL_RESET,

  __TABLENAME_UPPER___UPDATE_REQUEST,
  __TABLENAME_UPPER___UPDATE_SUCCESS,
  __TABLENAME_UPPER___UPDATE_FAIL,
  __TABLENAME_UPPER___UPDATE_RESET,

  __TABLENAME_UPPER___DELETE_REQUEST,
  __TABLENAME_UPPER___DELETE_SUCCESS,
  __TABLENAME_UPPER___DELETE_FAIL,
  __TABLENAME_UPPER___DELETE_RESET,

// akhir import actions
} from './__TABLENAME_LOWER__Constants'

// extra imports

export const __TABLENAME_LOWER__Create = () => async (dispatch, getState) => {
  try {
    dispatch({
      type: __TABLENAME_UPPER___CREATE_REQUEST
    })
    const {
      userLogin: { userInfo },
    } = getState()
    const { data } = await axios.post(
      config.serverPath(config.backend.paths.__TABLENAME_LOWER__Create.path),
      {},
      {
        headers: {
          'Content-type': 'application/json',
          Authorization: `Bearer ${userInfo.token}`
        }
      },
    )
    dispatch({
      type: __TABLENAME_UPPER___CREATE_SUCCESS,
      payload: data,
    })
    // extra create
  } catch (error) {
    dispatch({
      type: __TABLENAME_UPPER___CREATE_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
    })
  }
}

export const __TABLENAME_LOWER__List = (keyword = '') => async (dispatch) => {
  try {
    dispatch({
      type: __TABLENAME_UPPER___LIST_REQUEST
    })
    const { data } = await axios.get(
      config.serverPath(config.backend.paths.__TABLENAME_LOWER__List.path + `${keyword}`)
    )
    console.log(`
      __TABLENAME_LOWER__ list action terima:
      ${JSON.stringify(data, null, 2)}
    `);
    dispatch({
      type: __TABLENAME_UPPER___LIST_SUCCESS,
      payload: data,
    })
  } catch (error) {
    dispatch({
      type: __TABLENAME_UPPER___LIST_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
    })
  }
}

export const __TABLENAME_LOWER__ListPrivate = () => async (dispatch, getState) => {
  try {
    dispatch({
      type: __TABLENAME_UPPER___LIST_REQUEST
    })
    const { userLogin: { userInfo }, } = getState()
    const { data } = await axios.get(
      config.serverPath(config.backend.paths.__TABLENAME_LOWER__List.path)
    )
    console.log(`
      __TABLENAME_LOWER__ list action terima:
      ${JSON.stringify(data, null, 2)}
    `);
    dispatch({
      type: __TABLENAME_UPPER___LIST_SUCCESS,
      payload: data,
    })
  } catch (error) {
    dispatch({
      type: __TABLENAME_UPPER___LIST_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
    })
  }
}

export const __TABLENAME_LOWER__Detail = (id) => async (dispatch) => {
  try {
    dispatch({
      type: __TABLENAME_UPPER___DETAIL_REQUEST
    })
    // const {
    //   userLogin: { userInfo },
    // } = getState()
    const { data } = await axios.get(
      config.serverPath(config.backend.paths.__TABLENAME_LOWER__Detail.path + id),
      // {},
      // {
      //   headers: {
      //     'Content-type': 'application/json',
      //     Authorization: `Bearer ${userInfo.token}`
      //   }
      // },
    )
    dispatch({
      type: __TABLENAME_UPPER___DETAIL_SUCCESS,
      payload: data,
    })
  } catch (error) {
    dispatch({
      type: __TABLENAME_UPPER___DETAIL_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
    })
  }
}

export const __TABLENAME_LOWER__Update = (__TABLENAME_LOWER__) => async (dispatch, getState) => {
  try {
    dispatch({
      type: __TABLENAME_UPPER___UPDATE_REQUEST
    })
    const {
      userLogin: { userInfo },
    } = getState()
    const { data } = await axios.put(
      config.serverPath(config.backend.paths.__TABLENAME_LOWER__Update.path + __TABLENAME_LOWER__._id),
      __TABLENAME_LOWER__,
      {
        headers: {
          'Content-type': 'application/json',
          Authorization: `Bearer ${userInfo.token}`
        }
      },
    )
    dispatch({
      type: __TABLENAME_UPPER___UPDATE_SUCCESS,
      payload: data,
    })
  } catch (error) {
    dispatch({
      type: __TABLENAME_UPPER___UPDATE_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
    })
  }
}

export const __TABLENAME_LOWER__Delete = (id) => async (dispatch, getState) => {
  try {
    dispatch({
      type: __TABLENAME_UPPER___DELETE_REQUEST
    })
    const {
      userLogin: { userInfo },
    } = getState()
    const { data } = await axios.delete(      
      config.serverPath(config.backend.paths.__TABLENAME_LOWER__Delete.path + `${id}/`),
      // {},
      {
        headers: {
          'Content-type': 'application/json',
          Authorization: `Bearer ${userInfo.token}`
        }
      },
    )
    dispatch({
      type: __TABLENAME_UPPER___DELETE_SUCCESS,
      payload: data,
    })
  } catch (error) {
    dispatch({
      type: __TABLENAME_UPPER___DELETE_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
    })
  }
}

// akhir file actions