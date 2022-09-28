import React, { useState, useRef, useEffect } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import {default as ThemeButton} from '../components/Button';
import { TextField } from '@material-ui/core';
import Typography from '../components/Typography';
import ProductHeroLayout from './ProductHeroLayout';
import { Link } from "react-router-dom";
import "./styles.css"
import { InputAdornment } from '@material-ui/core';
import { ButtonGroup, Button, Grid, Box, Paper, Popper, Grow, MenuList, MenuItem } from '@mui/material';
import ClickAwayListener from '@mui/material/ClickAwayListener';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import { getRenderTemplates } from '../services/RenderService';

// const backgroundImage = 'https://metaphysic.ai/wp-content/uploads/2022/09/ARTICLE_montage-stable-diffusion.jpg';

const BACKUP_TEMPLATES = [
  {
      "pk": 2,
      "name": "Động vật",
      "description": "Tranh vẽ với chủ thể là các động vật trong tự nhiên"
  },
  {
      "pk": 3,
      "name": "Sản phẩm mẫu",
      "description": "Ảnh chụp cận cảnh các loại sản phẩm"
  },
  {
      "pk": 4,
      "name": "Tranh vẽ",
      "description": "Hình vẽ ngộ nghĩnh, đáng yêu bằng màu nước"
  },
  {
      "pk": 5,
      "name": "Chân dung",
      "description": "Ảnh chân dung người"
  },
  {
      "pk": 6,
      "name": "Tranh kĩ thuật số",
      "description": "Tranh được vẽ bằng máy tính trong môi trường 2D hoặc 3D"
  },
  {
      "pk": 7,
      "name": "Nội thất",
      "description": "Tranh nội thất, công trình kiến trúc"
  },
  {
      "pk": 39,
      "name": "Kiến trúc",
      "description": "Tranh vẽ các tòa nhà, công trình xây dựng"
  },
  {
      "pk": 40,
      "name": "Nhân vật hoạt hình",
      "description": "Sáng tạo các nhân vật hoạt hình ngộ nghĩnh, đáng yêu"
  },
  {
      "pk": 41,
      "name": "Viễn tưởng",
      "description": "Khung cảnh trong tương lai"
  },
  {
      "pk": 42,
      "name": "Tranh phong cảnh số",
      "description": "Tranh phong cảnh được vẽ trên máy tính"
  },
  {
      "pk": 43,
      "name": "Phong cảnh tự nhiên",
      "description": "Tranh phong cảnh tự nhiên như được chụp bằng máy ảnh"
  },
  {
      "pk": 44,
      "name": "Phác họa",
      "description": "Tranh phác họa bằng nét chì"
  },
  {
      "pk": 45,
      "name": "Steampunk",
      "description": "Tranh mang hơi hướng và phong cách của thời kì Victoria (thế kỉ 19 ở Anh)"
  },
  {
      "pk": 46,
      "name": "Vũ trụ",
      "description": "Tranh vẽ về các vật thể ngoài không gian"
  },
  {
      "pk": 47,
      "name": "Hậu tận thế",
      "description": "Tranh vẽ mang phong cách u tối của thế giới hậu tận thế"
  },
  {
      "pk": 1,
      "name": "Sáng tạo tự do",
      "description": "Trí tuệ nhân tạo tự do sáng tạo, không lệ thuộc vào một phong cách cụ thể nào"
  }
];


const styles = (theme) => ({
  background: {
    // backgroundImage: `url(${backgroundImage})`,
    backgroundColor: '#404040', // Average color of the background image.
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
  const anchorRef = useRef(null);
  const [open, setOpen] = useState(false);
  const [selectedTemplate, setselectedTemplate] = useState(null);

  const [templates, setTemplates] = useState([]);

  useEffect(() => {
    (async () => {
      try {
        const res = await getRenderTemplates();
        setTemplates(res);
      } catch (e) {
        setTemplates(BACKUP_TEMPLATES);
      }
    })();

  }, [])

  useEffect(() => {
    if (!templates || !templates.length) return;
    
    setselectedTemplate(templates[0]);
  }, [templates])

  const handleToggleTemplateButton = (e) => {
    setOpen((prevOpen) => !prevOpen);
  }

  const handleClose = (e) => {
    if (
      anchorRef.current &&
      anchorRef.current.contains(e.target)
    ) {
      return;
    }

    setOpen(false);
  };

  const handleMenuItemClick = (e, template) => {
    setselectedTemplate(template);
    setOpen(false);
  }


  return (
    <ProductHeroLayout backgroundClassName={classes.background}>
      {/* Increase the network loading priority of the background image. */}
      {/* <img style={{ display: 'none' }} src={backgroundImage} alt="increase priority" /> */}
      {/* <Typography color="inherit" align="center" variant="h2" marked="center"> */}

      <Typography align="center" variant="h2" style={{color: 'white'}}>
        Ứng dụng Trí tuệ nhân tạo<br></br>vẽ tranh minh họa theo cách dễ dàng nhất
      </Typography>

      <Box sx={{display: 'flex', width: '85%'}} mx={3} my={3} alignItems="center">
        <TextField
          className='inputRounded'
          placeholder="Một chú gà đang đi trong sân trong một ngày nắng đẹp"
          variant="outlined"
          InputProps={{
            startAdornment: <InputAdornment position="start">Tôi muốn vẽ: </InputAdornment>,
          }}
          style={{width: '100%', marginRight: '1em'}}
        />
        
        <ButtonGroup variant="contained">
          <ThemeButton variant="contained" size="large" color="primary" endIcon={<ArrowDropDownIcon/>} style={{borderRadius: '20px 0 0 20px', minWidth: '200px', whiteSpace: 'nowrap'}} onClick={handleToggleTemplateButton} ref={anchorRef}>
            {selectedTemplate && selectedTemplate.name}
          </ThemeButton>
          <ThemeButton
            color="secondary"
            variant="contained"
            size="large"
            style={{borderRadius: '0 20px 20px 0', minWidth: '180px', height: '60px'}}
          >
            Tạo tranh
          </ThemeButton>
        </ButtonGroup>
      </Box>
          
      
      
      <Typography variant="body2" color="inherit" className={classes.more} sx={{fontStyle:"italic"}}>
        *Chỉ 2.000đ cho một tranh minh họa
      </Typography>


      <Popper
        sx={{
          zIndex: 1,
        }}
        open={open}
        anchorEl={anchorRef.current}
        role={undefined}
        transition
        disablePortal
      >
        {({ TransitionProps, placement }) => (
          <Grow
            {...TransitionProps}
            style={{
              transformOrigin:
                placement === 'bottom' ? 'center top' : 'center bottom',
            }}
          >
            <Paper>
              <ClickAwayListener onClickAway={handleClose}>
                <MenuList id="split-button-menu" autoFocusItem>
                  {templates.map(template => (
                    <MenuItem
                      key={template.pk}
                      selected={template.pk === selectedTemplate.pk}
                      onClick={(event) => handleMenuItemClick(event, template)}
                    >
                      {template.name}
                    </MenuItem>
                  ))}
                </MenuList>
              </ClickAwayListener>
            </Paper>
          </Grow>
        )}
      </Popper>
          

    </ProductHeroLayout>
  );
}

ProductHero.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(ProductHero);