import { useEffect, useRef, useState } from 'react';
import { m } from 'framer-motion';
import { styled, useTheme } from '@mui/material/styles';
import { Button, Box, Link, Grid, Container, Typography, Stack, ButtonGroup, TextField, InputAdornment, Popper, Grow, MenuList, MenuItem, Paper, LinearProgress } from '@mui/material';
import { PATH_AUTH, PATH_DASHBOARD, PATH_PAGE } from '../../routes/paths';
import { MotionContainer, varFade } from '../../components/animate';
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import { getRenderTemplates, renderImage } from 'src/services/RenderService';
import ClickAwayListener from '@mui/material/ClickAwayListener';
import useAuth from 'src/hooks/useAuth';
import { useRouter } from 'next/router';
import { PromptTextField } from './PromptTextField';
import { RenderButtonGroup } from './RenderButtonGroup';
import { useSnackbar } from 'notistack';

const RootStyle = styled(m.div)(({ theme }) => ({
    position: 'relative',
    backgroundColor: theme.palette.grey[900],
    paddingTop: theme.spacing(10),
    [theme.breakpoints.up('md')]: {
        top: 0,
        left: 0,
        // position: 'fixed',
        width: '100%',
        height: '100%',
        // height: '50vh',
        display: 'flex',
        paddingTop: theme.spacing(25),
        // alignItems: 'center',
    },
}));


const RetryButton = (props) => {
    return (
        <Button variant="contained" color="primary" {...props}>Tạo lại</Button>
    )
}


export default function RenderPageContent() {
    const [rawPrompt, setRawPrompt] = useState('');
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const { query } = useRouter();
    const theme = useTheme();

    const { autoRender } = query;

    const { enqueueSnackbar } = useSnackbar();

    useEffect(() => {
        if (query.rawPrompt) {
            setRawPrompt(query.rawPrompt);
        }

        if (autoRender === 'true' && query.rawPrompt && query.templateId) {
            setLoading(true);
            (async () => {
                try {
                    const res = await renderImage(query.rawPrompt, parseInt(query.templateId), 512, 512, 1);
                    // const res = {
                    //     "status": 0,
                    //     "images": [
                    //         "https://replicate.com/api/models/stability-ai/stable-diffusion/files/7fd36274-3435-42e8-851a-f764d6ee91dc/out-0.png",
                    //         "https://replicate.com/api/models/stability-ai/stable-diffusion/files/7fd36274-3435-42e8-851a-f764d6ee91dc/out-0.png",
                    //         "https://replicate.com/api/models/stability-ai/stable-diffusion/files/7fd36274-3435-42e8-851a-f764d6ee91dc/out-0.png",
                    //         "https://replicate.com/api/models/stability-ai/stable-diffusion/files/7fd36274-3435-42e8-851a-f764d6ee91dc/out-0.png",
                    //     ],
                    //     "retry_count": 2,
                    //     "transaction_id": 605
                    // }
                    if (res.status === 0) {
                        setResult(res);
                    } 
                    else {
                        setResult(null);

                        // TODO: ghi ro loi dua tren res.status
                        enqueueSnackbar("Có lỗi xảy ra", {variant: 'error'});
                    }
                } catch(e) {
                    console.error(e);
                    enqueueSnackbar("Có lỗi xảy ra", {variant: 'error'});
                }

                setLoading(false);
            })();
            
        }
    }, [query])

    const handleRawPromptChange = (e) => {
        setRawPrompt(e.target.value);
    }

    const handleRenderButtonClick = async (templateId) => {
        setLoading(true);
        (async () => {
            try {
                const res = await renderImage(rawPrompt, parseInt(templateId), 512, 512, 4);
                if (res.status === 0) {
                    setResult(res);
                } 
                else {
                    setResult(null);

                    // TODO: ghi ro loi dua tren res.status
                    enqueueSnackbar("Có lỗi xảy ra", {variant: 'error'});
                }
            } catch(e) {
                console.error(e);
                enqueueSnackbar("Có lỗi xảy ra", {variant: 'error'});
            }

            setLoading(false);
        })();
    }

    return (
        <MotionContainer>
            <RootStyle>
                <Container maxWidth='100%'>
                    <Box sx={{display: 'flex', width: '100%', flexWrap: 'wrap', alignItems: 'center', justifyContent: 'center', gap: '1em 1em'}} my={5}>
                        <div style={{minWidth: '65%'}}>
                            <PromptTextField value={rawPrompt} onChange={handleRawPromptChange}/>
                        </div>
                        <RenderButtonGroup onSubmit={handleRenderButtonClick} defaultTemplateId={query.templateId}/>
                    </Box>

                    {loading && <LinearProgress my={3}/>}

                    {result &&
                    <Stack width="100%" alignItems="center" justifyContent="center">
                        <Grid container alignItems="center" justifyContent="space-between" spacing={2}>
                            {result.images.map((image, i) => 
                                <Grid item key={i} xs={6} sm={3}>
                                    <img src={image} style={{marginLeft: 'auto', marginRight: 'auto'}} />
                                </Grid>
                                
                            )}
                        </Grid>
                        <Typography my={3}>Chưa ưng ý với bức ảnh? Bạn có thể thử lại lần nữa. </Typography>
                        <RetryButton/>
                        <Typography my={3}>Bạn còn <span style={{color: theme.palette.primary.main}}>{result.retry_count}</span> lượt thử miễn phí</Typography>
                    </Stack>}
                </Container>
            </RootStyle>
        </MotionContainer>
    )
}