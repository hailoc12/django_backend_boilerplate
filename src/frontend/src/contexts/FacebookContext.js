import { createContext, useEffect, useReducer } from 'react';
import PropTypes from 'prop-types';
import { Auth0Client } from '@auth0/auth0-spa-js';
//
import { AUTH0_API } from '../config';
import { FACEBOOK_API } from '../config';
import { setSession } from 'src/utils/jwt';

// ----------------------------------------------------------------------

let auth0Client = null;

const initialState = {
  isAuthenticated: false,
  isInitialized: false,
  user: null,
};

const handlers = {
  INITIALIZE: (state, action) => {
    const { isAuthenticated, user } = action.payload;
    return { ...state, isAuthenticated, isInitialized: true, user };
  },
  LOGIN: (state, action) => {
    const { user } = action.payload;
    return { ...state, isAuthenticated: true, user };
  },
  LOGOUT: (state) => ({
    ...state,
    isAuthenticated: false,
    user: null,
  }),
};

const reducer = (state, action) => (handlers[action.type] ? handlers[action.type](state, action) : state);

const AuthContext = createContext({
  ...initialState,
  method: 'facebook',
  login: () => Promise.resolve(),
  logout: () => Promise.resolve(),
});

// ----------------------------------------------------------------------

AuthProvider.propTypes = {
  children: PropTypes.node,
};

function AuthProvider({ children }) {
  const [state, dispatch] = useReducer(reducer, initialState);

  useEffect(() => {
    const initialize = async () => {
      window.fbAsyncInit = function() {
        FB.init({
          appId            : FACEBOOK_API.appId,
          autoLogAppEvents : true,
          xfbml            : true,
          version          : 'v15.0',
        });
      };

      await window.fbAsyncInit();

      FB.getLoginStatus((response) => {
        const authResponse = response.authResponse;

        console.log(authResponse);

        if (response.status === 'connected') {
          // setSession(authResponse.accessToken);

          // DEBUG ONLY !!!
          setSession("14e3c93c93ee4f37169aff1664df4af90bad74ea");

          console.log('authResponse', authResponse);

          FB.api('/me', {fields: 'name,picture'}, (res) => {
            const user = {
              id: res.id,
              name: res.name,
              picture: res.picture?.data.url,
            }

            console.log('user', res);

            dispatch({
              type: 'INITIALIZE',
              payload: { isAuthenticated: true, user}
            })
          })
        }
        else {
          dispatch({
            type: 'INITIALIZE',
            payload: { isAuthenticated: false, user: null}
          })
        }
      });
    };

    initialize();
  }, []);

  const login = (onSuccess=()=>{}, onFailure=()=>{}) => {
    return FB.login(({ authResponse }) => {
      if (authResponse) {
        // setSession(authResponse.accessToken);
        setSession("14e3c93c93ee4f37169aff1664df4af90bad74ea");

        FB.api('/me', {fields: 'name,picture'}, function(response) {  
          const user = {
            id: response.id,
            name: response.name,
            picture: response.picture?.data.url,
          }

          onSuccess(user);
  
          dispatch({ type: 'LOGIN', payload: { user }});
        });
      } else {
        onFailure();
        console.log('User cancelled login or did not fully authorize.');
      }
    });    
  };

  const logout = () => {
    FB.logout((response) => {
      setSession(null);
      dispatch({ type: 'LOGOUT' });
    })
  };

  return (
    <AuthContext.Provider
      value={{
        ...state,
        method: 'facebook',
        user: {
          id: state?.user?.sub,
          photoURL: state?.user?.picture,
          email: state?.user?.email,
          displayName: state?.user?.name,
          role: 'user',
        },
        login,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export { AuthContext, AuthProvider };
