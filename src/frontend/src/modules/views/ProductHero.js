import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '../components/Button';
import { TextField } from '@material-ui/core';
import Typography from '../components/Typography';
import ProductHeroLayout from './ProductHeroLayout';
import { Link } from "react-router-dom";
import "./styles.css"
import { InputAdornment } from '@material-ui/core';


const backgroundImage = 'https://metaphysic.ai/wp-content/uploads/2022/09/ARTICLE_montage-stable-diffusion.jpg';

const styles = (theme) => ({
  background: {
    backgroundImage: `url(${backgroundImage})`,
    backgroundColor: '#7fc7d9', // Average color of the background image.
    backgroundPosition: 'center',
    // height: '100vh'
  },
  button: {
    minWidth: 200,
  },
  h5: {
    marginBottom: theme.spacing(4),
    marginTop: theme.spacing(4),
    [theme.breakpoints.up('sm')]: {
      marginTop: theme.spacing(10),
    },
  },
  more: {
    marginTop: theme.spacing(2),
  },
});

function ProductHero(props) {
  const { classes } = props;

  return (
    <ProductHeroLayout backgroundClassName={classes.background}>
      {/* Increase the network loading priority of the background image. */}
      {/* <img style={{ display: 'none' }} src={backgroundImage} alt="increase priority" /> */}
      {/* <Typography color="inherit" align="center" variant="h2" marked="center"> */}

      <Typography color="inherit" align="center" variant="h2">
        Ứng dụng Trí tuệ nhân tạo<br></br>vẽ tranh minh họa theo cách dễ dàng nhất
      </Typography>

      <TextField
        className='inputRounded'
        color="inherit"
        placeholder="Một chú gà đang đi trong sân trong một ngày nắng đẹp"
        variant="outlined"
        InputProps={{
          startAdornment: <InputAdornment position="start">Tôi muốn vẽ: </InputAdornment>,
        }}
      />

      <Link to={"/signup"} style={{ textDecoration: 'none' }}>
      <Button
        color="secondary"
        variant="contained"
        size="large"
        className={classes.button}
        component="a"
      >
        Tạo tranh
      </Button>
      </Link>
      <Typography variant="body2" color="inherit" className={classes.more} sx={{fontStyle:"italic"}}>
        *Chỉ 2.000đ cho một tranh minh họa
      </Typography>
    </ProductHeroLayout>
  );
}

ProductHero.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(ProductHero);