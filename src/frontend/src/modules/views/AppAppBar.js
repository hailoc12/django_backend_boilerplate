import React from "react";
import PropTypes from "prop-types";
import clsx from "clsx";
import { withStyles } from "@material-ui/core/styles";
import AppBar from "../components/AppBar";
import Toolbar, { styles as toolbarStyles } from "../components/Toolbar";
import { Link } from "react-router-dom";
import { Typography } from "@material-ui/core";

const styles = (theme) => ({
  title: {
    fontSize: 24,
    color: theme.palette.common.white,
  },
  placeholder: toolbarStyles(theme).root,
  toolbar: {
    justifyContent: "space-between",
  },
  left: {
    flex: 1,
  },
  leftLinkActive: {
    color: theme.palette.common.white,
  },
  right: {
    flex: 1,
    display: "flex",
    justifyContent: "flex-end",
  },
  rightLink: {
    fontSize: 16,
    color: theme.palette.common.white,
    marginLeft: theme.spacing(3),
  },
  linkSecondary: {
    color: theme.palette.secondary.main,
  },
});

function AppAppBar(props) {
  const { classes } = props;

  return (
    <div>
      <AppBar position="fixed">
        <Toolbar className={classes.toolbar}>
          <div className={classes.left}>
          <Link to={"/"} style={{ textDecoration: 'none' }}>
            <Typography
              variant="h6"
              underline="none"
              color="inherit"
              className={classes.title}
            >
              {"Vẽ minh họa"}
            </Typography>
          </Link>
          </div>
          {/* <div className={classes.center}>
          <Link to={"/"}>
            <Typography
              variant="h9"
              underline="none"
              color="inherit"
              className={classes.title}
            >
              {"Giới thiệu"}
            </Typography>
          </Link>
          </div> */}

          <div className={classes.right}>
            <Link to={"/about"} style={{ textDecoration: 'none' }}>
              <Typography
                variant="h6"
                underline="none"
                color="inherit"
                className={classes.rightLink}
              >
                {"Giới thiệu"}
              </Typography>
            </Link>
              
            <Link to={"/signin"} style={{ textDecoration: 'none' }}>
              <Typography
                color="inherit"
                variant="h6"
                underline="none"
                className={classes.rightLink}
              >
                {"Đăng nhập"}
              </Typography>
            </Link>
            <Link to={"/signup"} style={{ textDecoration: 'none' }}>
            <Typography
              variant="h6"
              underline="none"
              className={clsx(classes.rightLink, classes.linkSecondary)}
            >
              {"Đăng ký"}
            </Typography>
            </Link>
          </div>
        </Toolbar>
      </AppBar>
      <div className={classes.placeholder} />
    </div>
  );
}

AppAppBar.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(AppAppBar);
