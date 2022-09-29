import { useEffect, useRef, useState } from 'react';
import { m } from 'framer-motion';
// @mui
import { styled } from '@mui/material/styles';
import { Button, Box, Link, Container, Typography, Stack, ButtonGroup, TextField, InputAdornment } from '@mui/material';
// routes
import { PATH_AUTH, PATH_DASHBOARD, PATH_PAGE } from '../../routes/paths';
// components
import Image from '../../components/Image';
import Iconify from '../../components/Iconify';
import TextIconLabel from '../../components/TextIconLabel';
import { MotionContainer, varFade } from '../../components/animate';


import { useTheme } from '@mui/material/styles';
import useAuth from 'src/hooks/useAuth';
import { useRouter } from 'next/router';
import { RenderButtonGroup } from '../render/RenderButtonGroup';
import { PromptTextField } from '../render/PromptTextField';

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


// ----------------------------------------------------------------------

export default function HomeHero() {
  const [rawPrompt, setRawPrompt] = useState('');

  const { user, isAuthenticated } = useAuth();

  const router = useRouter();


  const handleRawPromptChange = (e) => {
    setRawPrompt(e.target.value);
  }

  const handleRenderButtonClick = async (templateId) => {
    // redirect to render page
    if (isAuthenticated) {
      router.push({pathname: PATH_PAGE.render, query: {rawPrompt, templateId: templateId, autoRender: true}});
    } else {
      router.push(PATH_AUTH.login);
    }
  }

  return (
    <MotionContainer>
      <RootStyle>
        <Container>
            <div style={{display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
              <m.div variants={varFade().inDown}>
                <Typography align="center" variant="h2" style={{color: 'white'}}>
                  Ứng dụng Trí tuệ nhân tạo<br></br>vẽ tranh minh họa theo cách dễ dàng nhất
                </Typography>
              </m.div>
              
              <Box sx={{display: 'flex', width: '100%', flexWrap: 'wrap', alignItems: 'center', justifyContent: 'center', gap: '1em 0'}} my={5}>
                <m.div variants={varFade().inLeft} style={{marginRight: '1em', minWidth: '65%'}}>
                  <PromptTextField value={rawPrompt} onChange={handleRawPromptChange}/>
                </m.div>
                <m.div variants={varFade().inRight}>
                  <RenderButtonGroup onSubmit={handleRenderButtonClick}/>
                </m.div>
              </Box>

              <m.div variants={varFade().inUp}>
                <Typography variant="body" sx={{fontStyle:"italic"}}>
                  *Chỉ 2.000đ cho một tranh minh họa
                </Typography>
              </m.div>
            </div>

        </Container>
      </RootStyle>
    </MotionContainer>
  );
}
