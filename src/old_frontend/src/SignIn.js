import withRoot from './modules/withRoot';
// --- Post bootstrap -----
import React, { useState } from 'react';
import { Link } from "react-router-dom";
import {
  Box,
  // Button,
  TextField,
  makeStyles,
} from "@material-ui/core";
import { Button, Card, CardContent, Grid, Typography } from '@mui/material';
// import Typography from './modules/components/Typography';
import AppFooter from './modules/views/AppFooter';
import AppAppBar from './modules/views/AppAppBar';
import AppForm from './modules/views/AppForm';
import * as Yup from "yup";
import { Formik } from "formik";

// import FacebookLogin from 'react-facebook-login';
import FacebookLogin from 'react-facebook-login/dist/facebook-login-render-props';
import FacebookIcon from '@mui/icons-material/Facebook';
import { signIn, signOut } from './modules/services/FacebookService';

// const backgroundImage = 'https://metaphysic.ai/wp-content/uploads/2022/09/ARTICLE_montage-stable-diffusion.jpg';
const backgroundImage = '/background.jpg';

const useStyles = makeStyles((theme) => ({
  form: {
    marginTop: theme.spacing(6),
  },
  button: {
    marginTop: theme.spacing(3),
    marginBottom: theme.spacing(2),
  },
  feedback: {
    marginTop: theme.spacing(2),
  },
  background: {
    backgroundImage: `url(${backgroundImage})`,
    // backgroundImage: 'url(/background.jpg)',
    backgroundColor: '#000',
    backgroundPosition: 'center',
    backgroundSize: 'cover',
    // height: '100vh'
  },
}));

function SignIn() {
  const styles = useStyles();
  const [loading, setLoading] = useState(false);

  const responseFacebook = (response) => {
    console.log('facebook', response);
  }

  const handleSignInWithFacebook = async (e) => {
    try {
      await signIn();
    }
    catch(e) {
      await signOut();
    }
  }

  return (
    <>
      <AppAppBar />

      <Box style={{backgroundColor: 'black', position: 'relative', height: '80vh'}}>
        <Grid container style={{position: 'absolute', height: '80vh', opacity: 0.5}} className={styles.background}></Grid>
        
        
        <Grid container direction="column" alignItems="center" position="relative">
          <Grid item xs={12}>
              <Card style={{ minHeight: "50vh", padding: "3rem", margin: "4rem 1rem 0rem 1rem", backgroundColor: "rgba(0,0,0,0.8)"}}>
                <CardContent>
                  <Typography variant="h5" mb={5} color="white"><b>Đăng nhập</b></Typography>
                  {/* <FacebookLogin
                    appId="614342580170103"
                    // autoLoad
                    callback={responseFacebook}
                    render={renderProps => (
                      <Button variant='contained' onClick={renderProps.onClick} startIcon={<FacebookIcon/>} size="large">Đăng nhập bằng Facebook</Button>
                  )}
                  /> */}
                  <Button variant="contained" sx={{backgroundColor: "#1675d1"}} startIcon={<FacebookIcon/>} size="large" onClick={handleSignInWithFacebook}>Đăng nhập bằng Facebook</Button>

                </CardContent>
              </Card>
          </Grid>
        </Grid>
      

      </Box>
      

      <AppFooter/>
      
      


      {/* <AppForm>
      
        <Typography variant="h3" gutterBottom marked="center" align="center">
          Sign In
        </Typography>
        <Typography variant="body2" align="center">
          {'Not a member yet? '}
          <Link to={"/signup"} align="center" underline="always">
            Sign Up here
          </Link>
        </Typography>
        
        <Formik
            initialValues={{
              email: "",
              password: "",
            }}
            validationSchema={Yup.object().shape({
              email: Yup.string()
                .email("Must be a valid email")
                .max(255)
                .required("Email is required"),
              password: Yup.string()
                .max(255)
                .required("Password is required"),
            })}
            onSubmit={async (values) => {
              try {
                window.location.reload();
              } catch (e) {
                alert(e.message);
              }
            }}
          >
            {({
              errors,
              handleBlur,
              handleSubmit,
              handleChange,
              isSubmitting,
              touched,
              values,
            }) => (
              <form onSubmit={handleSubmit}>

                <TextField
                  error={Boolean(touched.email && errors.email)}
                  fullWidth
                  helperText={touched.email && errors.email}
                  label="Email Address"
                  margin="normal"
                  name="email"
                  onBlur={handleBlur}
                  onChange={handleChange}
                  type="email"
                  value={values.email}
                  variant="outlined"
                />
                <TextField
                  error={Boolean(touched.password && errors.password)}
                  fullWidth
                  helperText={touched.password && errors.password}
                  label="Password"
                  margin="normal"
                  name="password"
                  onBlur={handleBlur}
                  onChange={handleChange}
                  type="password"
                  value={values.password}
                  variant="outlined"
                />
                <Box my={2}>
                  <Button
                    color="primary"
                    disabled={isSubmitting}
                    fullWidth
                    size="large"
                    type="submit"
                    variant="contained"
                  >
                    Sign in now
                  </Button>
                </Box>
                <Typography color="textSecondary" variant="body1">
                  Don&apos;t have an account?{" "}
                  <Link to={"/signup"} variant="h6">
                    Sign upp
                  </Link>
                </Typography>
              </form>
            )}
        </Formik>
      </AppForm> */}
      
    </>
  );
}

export default withRoot(SignIn);
