import { Box, Button, CircularProgress, IconButton, styled } from "@mui/material";
import SearchIcon from '@mui/icons-material/Search';
import { useState } from "react";
import { m } from 'framer-motion';



const BlankStyle = styled('div')(({ theme }) => ({
    backgroundColor: theme.palette.grey[600],
    width: 'auto',
    height: '25vh',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
}));


export default function ResultItem({src, onClick}) {
    const [show, setShow] = useState(false);
    const [loaded, setLoaded] = useState(false);

    const handleMouseEnter = () => {
        setShow(true);
    }

    const handleMouseLeave = () => {
        setShow(false);
    }

    const handleSearchClick = () => {
        console.log('TODO');
    }

    const handleImageClick = () => {
        onClick();
    }

    const handleImageLoad = () => {
        setLoaded(true);
    }

    return (
        <Box sx={{borderRadius: '10px', overflow: 'hidden', position: 'relative'}} onMouseEnter={handleMouseEnter} onMouseLeave={handleMouseLeave}>
            {!loaded && 
            <BlankStyle>
                <CircularProgress color='primary'/>
            </BlankStyle>
            }
            <img src={src} style={{marginLeft: 'auto', marginRight: 'auto', visibility: loaded ? 'visible' : 'collapse'}} onClick={handleImageClick} onLoad={handleImageLoad}/>

            {loaded && <IconButton variant="outlined" sx={{position: 'absolute', top: '5px', left: '5px', visibility: show ? 'visible' : 'collapse'}} onClick={handleSearchClick}>
                <SearchIcon />
            </IconButton>}
        </Box>
    )
}