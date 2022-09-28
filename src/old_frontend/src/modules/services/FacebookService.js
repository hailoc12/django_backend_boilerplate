import { useHistory } from "react-router-dom";


export const signIn = async () => {
    const { authResponse } = await window.FB.login();
    if (!authResponse) return;

    const response = await window.FB.api('/me');

    console.log('response', response)

    // window.FB.login(function(response) {
    //     if (response.authResponse) {
    //      console.log('Welcome!  Fetching your information.... ');
    //      FB.api('/me', function(response) {
    //        console.log('Good to see you, ' + response.name + '.');
    //      });
    //     } else {
    //      console.log('User cancelled login or did not fully authorize.');
    //     }
    // });
}

export const signOut = async () => {
    // revoke app permissions to logout completely because FB.logout() doesn't remove FB cookie
    window.FB.api('/me/permissions', 'delete', null, () => window.FB.logout());
    // stopAuthenticateTimer();
    // accountSubject.next(null);
    // history.push('/login');
}



// export const login = async () => {
//     // login with facebook then authenticate with the API to get a JWT auth token
//     const { authResponse } = await new Promise(window.FB.login);
//     if (!authResponse) return;

//     // await apiAuthenticate(authResponse.accessToken);

//     // // get return url from location state or default to home page
//     // const { from } = history.location.state || { from: { pathname: "/" } };
//     // history.push(from);
// }
