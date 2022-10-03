import { useEffect, useRef, useState } from 'react';
import { m } from 'framer-motion';
import { styled, useTheme } from '@mui/material/styles';
import { Button, Box, Link, Grid, Container, Typography, Stack, LinearProgress } from '@mui/material';
import { MotionContainer } from '../../components/animate';
import { useRouter } from 'next/router';
import { PromptTextField } from './PromptTextField';
import { RenderButtonGroup } from './RenderButtonGroup';
import { useSnackbar } from 'notistack';
import ResultItem from './ResultItem';
import GalleryItemModal from './GalleryItemModal';
import { renderImage } from 'src/services/RenderService';


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
        paddingTop: theme.spacing(10),
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
    const [openModal, setOpenModal] = useState(false);
    const [selectedItem, setSelectedItem] = useState(null);

    const router = useRouter();
    const { pathname, query } = router;
    
    const theme = useTheme();

    const { autoRender } = query;

    const { enqueueSnackbar } = useSnackbar();


    const removeQueryParam = (param) => {
        const params = new URLSearchParams(query);
        params.delete(param);
        router.replace(
            { pathname, query: params.toString() },
            undefined, 
            { shallow: true }
        );
    };

    useEffect(() => {
        if (query.rawPrompt) {
            setRawPrompt(query.rawPrompt);
        }

        if (autoRender === 'true' && query.rawPrompt && query.templateId) {
            console.log('Auto render');
            removeQueryParam('autoRender');
            render(query.rawPrompt, parseInt(query.templateId));
        }
    }, [query])

    const render = async (overridedRawPrompt=undefined, overridedTemplateId=undefined) => {
        console.log('Rendering...', overridedRawPrompt || rawPrompt, overridedTemplateId || parseInt(query.templateId));
        setLoading(true);
        try {
            await new Promise(r => setTimeout(r, 2000));
            const res = await renderImage(overridedRawPrompt || rawPrompt, overridedTemplateId || parseInt(query.templateId), 512, 512, 1);
            // const res = {
            //     "status": 0,
            //     "images": [
            //         "https://replicate.com/api/models/stability-ai/stable-diffusion/files/7fd36274-3435-42e8-851a-f764d6ee91dc/out-0.png",
            //         "https://replicate.com/api/models/stability-ai/stable-diffusion/files/7fd36274-3435-42e8-851a-f764d6ee91dc/out-0.png",
            //         "https://image.lexica.art/md/085ee24c-8473-430b-a831-9cdef41972a9",
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
        console.log('Finished rendering');
    }

    const handleRawPromptChange = (e) => {
        setRawPrompt(e.target.value);
    }

    const handleRenderButtonClick = async (templateId) => {
        setLoading(true);
        render();
    }

    const handleCloseModal = () => {
        setOpenModal(false);
    }

    const handleClickItem = (item) => {
        setOpenModal(true);
        setSelectedItem(item);
    }

    const handleRetry = () => {
        console.log('retrying...');
        setResult(null);
        render();
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
                        <Grid container alignItems="start" justifyContent="space-evenly" spacing={2}>
                            {result.images.map((image, i) => 
                                <Grid item key={i} xs={6} sm={3}>
                                    <ResultItem src={image} onClick={() => handleClickItem({url: image, prompt: rawPrompt})}/>
                                </Grid>
                            )}
                        </Grid>
                        <Typography my={3}>Chưa ưng ý với bức ảnh? Bạn có thể thử lại lần nữa. </Typography>
                        <RetryButton onClick={handleRetry}/>
                        {result && <Typography my={3}>Bạn còn <span style={{color: theme.palette.primary.main}}>{result.retry_count}</span> lượt thử miễn phí</Typography>}
                    </Stack>}

                    <GalleryItemModal open={openModal} onClose={handleCloseModal} item={selectedItem}/>

                </Container>
            </RootStyle>
        </MotionContainer>
    )
}