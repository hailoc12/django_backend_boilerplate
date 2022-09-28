import { useEffect, useRef, useState } from 'react';
import { m } from 'framer-motion';
import NextLink from 'next/link';
// @mui
import { styled } from '@mui/material/styles';
import { Button, Box, Link, Container, Typography, Stack, ButtonGroup, TextField, InputAdornment, Popper, Grow, MenuList, MenuItem, Paper } from '@mui/material';
// routes
import { PATH_DASHBOARD } from '../../routes/paths';
// components
import Image from '../../components/Image';
import Iconify from '../../components/Iconify';
import TextIconLabel from '../../components/TextIconLabel';
import { MotionContainer, varFade } from '../../components/animate';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import { getRenderTemplates } from 'src/services/RenderService';
import ClickAwayListener from '@mui/material/ClickAwayListener';
import { useTheme } from '@mui/material/styles';
import useAuth from 'src/hooks/useAuth';

// ----------------------------------------------------------------------

const RootStyle = styled(m.div)(({ theme }) => ({
  position: 'relative',
  backgroundColor: theme.palette.grey[900],
  paddingTop: theme.spacing(15),
  [theme.breakpoints.up('md')]: {
    top: 0,
    left: 0,
    // position: 'fixed',
    width: '100%',
    // height: '100vh',
    height: '50vh',
    display: 'flex',
    paddingTop: theme.spacing(25),
    // alignItems: 'center',
  },
}));

const ContentStyle = styled((props) => <Stack spacing={5} {...props} />)(({ theme }) => ({
  zIndex: 10,
  maxWidth: 520,
  margin: 'auto',
  textAlign: 'center',
  position: 'relative',
  paddingTop: theme.spacing(15),
  paddingBottom: theme.spacing(15),
  [theme.breakpoints.up('md')]: {
    margin: 'unset',
    textAlign: 'left',
  },
}));

const HeroOverlayStyle = styled(m.img)({
  zIndex: 9,
  width: '100%',
  height: '100%',
  objectFit: 'cover',
  position: 'absolute',
});

const HeroImgStyle = styled(m.img)(({ theme }) => ({
  top: 0,
  right: 0,
  bottom: 0,
  zIndex: 8,
  width: '100%',
  margin: 'auto',
  position: 'absolute',
  [theme.breakpoints.up('lg')]: {
    right: '8%',
    width: 'auto',
    height: '48vh',
  },
}));

const backupTemplates = [
  {
    "pk": 3,
    "name": "Sản phẩm mẫu",
    "description": "Ảnh chụp cận cảnh các loại sản phẩm"
  },
  {
    "pk": 2,
    "name": "Động vật",
    "description": "Tranh vẽ với chủ thể là các động vật trong tự nhiên"
  },
];



const StyledTextField = styled(TextField)({
  '& input:valid + fieldset': {
    borderWidth: 0,
  },
  '& input:invalid + fieldset': {
    borderWidth: 0,
  },
  '& .MuiOutlinedInput-root': {
    '&.Mui-focused fieldset': {
      borderWidth: 0,
    },
  },
});

const TemplateButton = styled(Button)(({ theme }) => ({
  // color: theme.palette.getContrastText(purple[500]),
  backgroundColor: theme.palette.grey[700],
  '&:hover': {
    backgroundColor: theme.palette.grey[800],
  },
}));


// ----------------------------------------------------------------------

export default function HomeHero() {
  const anchorRef = useRef(null);
  const [open, setOpen] = useState(false);
  const [selectedTemplate, setselectedTemplate] = useState(null);

  const [templates, setTemplates] = useState([]);

  const { user, isAuthenticated } = useAuth();

  useEffect(() => {
    (async () => {
      try {
        const res = await getRenderTemplates();
        setTemplates(res);
      } catch (e) {
        setTemplates(backupTemplates);
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
    <MotionContainer>
      <RootStyle>
        {/* <HeroOverlayStyle
          alt="overlay"
          src="https://minimal-assets-api.vercel.app/assets/overlay.svg"
          variants={varFade().in}
        />

        <HeroImgStyle
          alt="hero"
          src="https://minimal-assets-api.vercel.app/assets/images/home/hero.png"
          variants={varFade().inUp}
        /> */}

        <Container>
            <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
              <m.div variants={varFade().inDown}>
                <Typography align="center" variant="h2" style={{color: 'white'}}>
                  Ứng dụng Trí tuệ nhân tạo<br></br>vẽ tranh minh họa theo cách dễ dàng nhất
                </Typography>
              </m.div>
              
              <Box sx={{display: 'flex', width: '100%', flexWrap: 'wrap', alignItems: 'center', justifyContent: 'center', gap: '1em 0'}} my={5}>
                <m.div variants={varFade().inLeft} style={{marginRight: '1em', minWidth: '65%'}}>
                  <StyledTextField
                    placeholder="Một chú gà đang đi trong sân trong một ngày nắng đẹp"
                    variant="outlined"
                    InputProps={{
                      startAdornment: <InputAdornment position="start">Tôi muốn vẽ: </InputAdornment>,
                    }}
                    style={{backgroundColor: 'white', borderRadius: '20px', width: '100%'}}
                  />
                </m.div>
                
                <m.div variants={varFade().inRight}>
                  <ButtonGroup variant="contained" size='large' disableElevation={true}>
                    <TemplateButton endIcon={<ArrowDropDownIcon/>} style={{borderRadius: '20px 0 0 20px', whiteSpace: 'nowrap', height: '60px'}} onClick={handleToggleTemplateButton} ref={anchorRef}>
                      {selectedTemplate && selectedTemplate.name}
                    </TemplateButton>
                    <Button
                      sx={{borderRadius: '0 20px 20px 0', whiteSpace: 'nowrap', minWidth: '200px', height: '60px'}}
                    >
                      Tạo tranh
                    </Button>
                  </ButtonGroup>
                </m.div>
                
              </Box>


              <m.div variants={varFade().inUp}>
                <Typography variant="body" sx={{fontStyle:"italic"}}>
                  *Chỉ 2.000đ cho một tranh minh họa
                </Typography>
              </m.div>
            </div>

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

          {/* <ContentStyle>
            <m.div variants={varFade().inRight}>
              <Typography variant="h1" sx={{ color: 'common.white' }}>
                Start a <br />
                new project <br /> with
                <Typography component="span" variant="h1" sx={{ color: 'primary.main' }}>
                  &nbsp;Minimal
                </Typography>
              </Typography>
            </m.div>

            <m.div variants={varFade().inRight}>
              <Typography sx={{ color: 'common.white' }}>
                The starting point for your next project based on easy-to-customize MUI helps you build apps faster and
                better.
              </Typography>
            </m.div>

            <Stack spacing={2.5} alignItems="center" direction={{ xs: 'column', md: 'row' }}>
              <m.div variants={varFade().inRight}>
                <TextIconLabel
                  icon={
                    <Image
                      alt="sketch icon"
                      src="https://minimal-assets-api.vercel.app/assets/images/home/ic_sketch_small.svg"
                      sx={{ width: 20, height: 20, mr: 1 }}
                    />
                  }
                  value={
                    <Link
                      href="https://www.sketch.com/s/0fa4699d-a3ff-4cd5-a3a7-d851eb7e17f0"
                      target="_blank"
                      rel="noopener"
                      color="common.white"
                      sx={{ typography: 'body2' }}
                    >
                      Preview Sketch
                    </Link>
                  }
                />
              </m.div>

              <m.div variants={varFade().inRight}>
                <TextIconLabel
                  icon={
                    <Image
                      alt="sketch icon"
                      src="https://minimal-assets-api.vercel.app/assets/images/home/ic_figma_small.svg"
                      sx={{ width: 20, height: 20, mr: 1 }}
                    />
                  }
                  value={
                    <Link
                      href="https://www.figma.com/file/x7earqGD0VGFjFdk5v2DgZ/%5BPreview%5D-Minimal-Web?node-id=866%3A55474"
                      target="_blank"
                      rel="noopener"
                      color="common.white"
                      sx={{ typography: 'body2' }}
                    >
                      Preview Figma
                    </Link>
                  }
                />
              </m.div>
            </Stack>

            <m.div variants={varFade().inRight}>
              <NextLink href={PATH_DASHBOARD.root} passHref>
                <Button
                  size="large"
                  variant="contained"
                  startIcon={<Iconify icon={'eva:flash-fill'} width={20} height={20} />}
                >
                  Live Preview
                </Button>
              </NextLink>
            </m.div>

            <Stack spacing={2.5}>
              <m.div variants={varFade().inRight}>
                <Typography variant="overline" sx={{ color: 'primary.light' }}>
                  Available For
                </Typography>
              </m.div>

              <Stack direction="row" spacing={1.5} justifyContent={{ xs: 'center', md: 'flex-start' }}>
                {['ic_sketch', 'ic_figma', 'ic_js', 'ic_ts', 'ic_nextjs'].map((resource) => (
                  <m.img
                    key={resource}
                    variants={varFade().inRight}
                    src={`https://minimal-assets-api.vercel.app/assets/images/home/${resource}.svg`}
                  />
                ))}
              </Stack>
            </Stack>
          </ContentStyle> */}
        </Container>
      </RootStyle>
      {/* <Box sx={{ height: { md: '100vh' } }} /> */}
    </MotionContainer>
  );
}
