import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import Typography from '../components/Typography';
import TextField from '../components/TextField';
import { Link, withStyles } from '@mui/material';

function Copyright(props) {
  return (
    <>
      <span {...props}>{'© '}</span>
      <Link href="https://aivgroup.vn/" {...props}>
        AIV Group
      </Link>{' '}
      <span {...props}>{new Date().getFullYear()}</span>
    </>
  );
}

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    // backgroundColor: theme.palette.secondary.light,
    backgroundColor: theme.palette.primary.dark,
  },
  link: {
    color: theme.palette.common.white,
  },
  
  container: {
    marginTop: theme.spacing(8),
    marginBottom: theme.spacing(8),
    display: 'flex',
  },
  iconsWrapper: {
    height: 120,
  },
  icons: {
    display: 'flex',
  },
  icon: {
    width: 48,
    height: 48,
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: theme.palette.warning.main,
    marginRight: theme.spacing(1),
    '&:hover': {
      backgroundColor: theme.palette.warning.dark,
    },
  },
  list: {
    margin: 0,
    listStyle: 'none',
    padding: 0,
  },
  listItem: {
    paddingTop: theme.spacing(0.5),
    paddingBottom: theme.spacing(0.5),
  },
  language: {
    marginTop: theme.spacing(1),
    width: 150,
  },
}));

const LANGUAGES = [
  {
    code: 'vi-VN',
    name: 'Tiếng Việt',
  },
  {
    code: 'en-US',
    name: 'English',
  },
  // {
  //   code: 'fr-FR',
  //   name: 'Français',
  // },
];

export default function AppFooter() {
  const classes = useStyles();

  return (
    <Typography component="footer" className={classes.root}>
      <Container className={classes.container}>
        <Grid container>
          <Grid item xs={6}>
            <Grid
              container
              direction="column"
              justifyContent="flex-end"
              className={classes.iconsWrapper}
              spacing={2}
            >
              <Grid item className={classes.icons}>
                <a href="https://material-ui.com/" className={classes.icon}>
                  <img src="/appFooterFacebook.png" alt="Facebook" />
                </a>
                <a href="https://twitter.com/MaterialUI" className={classes.icon}>
                  <img src="/appFooterTwitter.png" alt="Twitter" />
                </a>
              </Grid>
              <Grid item>
                <Copyright style={{color: 'white'}} />
              </Grid>
            </Grid>
          </Grid>
          <Grid item xs={6}>
            <Typography variant="h6" marked="left" style={{color: 'white'}} gutterBottom>
              Pháp lý
            </Typography>
            <ul className={classes.list}>
              <li className={classes.listItem}>
                <Link href="/terms" style={{color: 'white'}}>Điều khoản sử dụng</Link>
              </li>
              <li className={classes.listItem}>
                <Link href="/privacy" style={{color: 'white'}}>Quyền riêng tư</Link>
              </li>
            </ul>
          </Grid>
          {/* <Grid item xs={4}>
            <Typography variant="h6" marked="left" gutterBottom>
              Ngôn ngữ
            </Typography>
            <TextField
              select
              SelectProps={{
                native: true,
              }}
              className={classes.language}
            >
              {LANGUAGES.map((language) => (
                <option value={language.code} key={language.code}>
                  {language.name}
                </option>
              ))}
            </TextField>
          </Grid> */}
        </Grid>
      </Container>
    </Typography>
  );
}
