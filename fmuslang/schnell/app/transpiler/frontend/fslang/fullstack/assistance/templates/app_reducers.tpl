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

// akhir import reducers
} from './__TABLENAME_LOWER__Constants'

export const __TABLENAME_LOWER__CreateReducer = (state = {}, action) => {
  switch (action.type) {
    case __TABLENAME_UPPER___CREATE_REQUEST:
      return { loading: true }
    case __TABLENAME_UPPER___CREATE_SUCCESS:
      return { loading: false, success: true, __TABLENAME_LOWER__: action.payload }
    case __TABLENAME_UPPER___CREATE_FAIL:
      return { loading: false, error: action.payload }
    case __TABLENAME_UPPER___CREATE_RESET:
      return {}
    default:
      return state    
  }
}

export const __TABLENAME_LOWER__ListReducer = (state = { __TABLENAME_LOWER__s: []}, action) => {
  switch (action.type) {
    case __TABLENAME_UPPER___LIST_REQUEST:
      return { loading: true, __TABLENAME_LOWER__s: [] }
    case __TABLENAME_UPPER___LIST_SUCCESS:
      return {
        loading: false,
        __TABLENAME_LOWER__s: action.payload.__TABLENAME_LOWER__s,
        page: action.payload.page,
        pages: action.payload.pages
      }
    case __TABLENAME_UPPER___LIST_FAIL:
      return { loading: false, error: action.payload }
    case __TABLENAME_UPPER___LIST_RESET:
      return {}
    default:
      return state    
  }
}

export const __TABLENAME_LOWER__DetailReducer = (state = { __TABLENAME_LOWER__: {} }, action) => {
  switch (action.type) {
    case __TABLENAME_UPPER___DETAIL_REQUEST:
      return { loading: true, ...state }
    case __TABLENAME_UPPER___DETAIL_SUCCESS:
      return { loading: false, __TABLENAME_LOWER__: action.payload }
    case __TABLENAME_UPPER___DETAIL_FAIL:
      return { loading: false, error: action.payload }
    case __TABLENAME_UPPER___DETAIL_RESET:
      return {}
    default:
      return state    
  }
}

export const __TABLENAME_LOWER__UpdateReducer = (state = { __TABLENAME_LOWER__: {} }, action) => {
  switch (action.type) {
    case __TABLENAME_UPPER___UPDATE_REQUEST:
      return { loading: true }
    case __TABLENAME_UPPER___UPDATE_SUCCESS:
      return { loading: false, success: true, __TABLENAME_LOWER__: action.payload }
    case __TABLENAME_UPPER___UPDATE_FAIL:
      return { loading: false, error: action.payload }
    case __TABLENAME_UPPER___UPDATE_RESET:
      return { __TABLENAME_LOWER__: {} }
    default:
      return state    
  }
}

export const __TABLENAME_LOWER__DeleteReducer = (state = {}, action) => {
  switch (action.type) {
    case __TABLENAME_UPPER___DELETE_REQUEST:
      return { loading: true }
    case __TABLENAME_UPPER___DELETE_SUCCESS:
      return { loading: false, success: true }
    case __TABLENAME_UPPER___DELETE_FAIL:
      return { loading: false, error: action.payload }
    case __TABLENAME_UPPER___DELETE_RESET:
      return {}
    default:
      return state    
  }
}

// akhir file reducers