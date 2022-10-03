import { Box, Grid, Modal, Backdrop, Button, Fade, Typography, styled, Stack } from "@mui/material";
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import DownloadIcon from '@mui/icons-material/Download';
import IosShareIcon from '@mui/icons-material/IosShare';
import { useSnackbar } from "notistack";
import { saveAs } from 'file-saver';

const styles = {
    modal: {
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 400,
        bgcolor: 'background.paper',
        border: '2px solid #000',
        boxShadow: 24,
        p: 4,
    }
}

const RootStyle = styled(Grid)(({ theme }) => ({
    backgroundColor: theme.palette.background.paper,
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: '100%',
    minHeight: '70vh',
    maxHeight: '90vh',
    // bgcolor: 'background.paper',
    // border: '2px solid #000',
    // boxShadow: 24,
    padding: '1.5em',
    borderRadius: '10px',

    // paddingTop: theme.spacing(15),
    [theme.breakpoints.up('md')]: {
    //   top: 0,
    //   left: 0,
    //   // position: 'fixed',
      
      width: '800px',
    //   // height: '100vh',
    //   height: '50vh',
    //   display: 'flex',
    //   paddingTop: theme.spacing(25),
    //   // alignItems: 'center',
    },
  }));
  
const BoxPromptStyle = styled(Box)(({ theme }) => ({
    backgroundColor: theme.palette.grey[700],
    padding: '1em',
    borderRadius: '10px',
}));


export default function GalleryItemModal({open, onClose, item}) {
    const { enqueueSnackbar } = useSnackbar();

    const handleCopyPrompt = () => {
        navigator.clipboard.writeText(item.prompt);
        enqueueSnackbar("Đã sao chép");
    }

    const handleDownload = () => {
        saveAs(item.url, "output.png");
    }

    return (
        <Modal open={open} onClose={onClose}
            closeAfterTransition
            BackdropComponent={Backdrop}
            BackdropProps={{
            timeout: 500,
            }}  
        >
            <Fade in={open}>
                <RootStyle container columnSpacing={1}>
                        <Grid item xs={12} md={5}>
                            <Stack spacing={2}>
                                <BoxPromptStyle>
                                    <Typography variant='body1'>{item?.prompt}</Typography>
                                    
                                </BoxPromptStyle>

                                <div style={{display: 'flex', gap: '10px', flexWrap: 'wrap'}}>
                                    <Button variant='outlined' color='secondary' startIcon={<ContentCopyIcon/>} onClick={handleCopyPrompt}>Sao chép lệnh</Button>
                                    <Button variant='outlined' color='secondary' startIcon={<DownloadIcon/>} onClick={handleDownload}>Tải xuống</Button>
                                    <Button variant='outlined' color='primary' startIcon={<IosShareIcon/>}>Chia sẻ</Button>
                                </div>
                            </Stack>
                        </Grid>
                        <Grid item xs={12} md={7}>
                            {item && <img src={item.url}/>}
                        </Grid>
                    
                </RootStyle>
                
            </Fade>
        </Modal>
    )
}



// export default function TransitionsModal() {
//   const [open, setOpen] = React.useState(false);
//   const handleOpen = () => setOpen(true);
//   const handleClose = () => setOpen(false);

//   return (
//     <div>
//       <Button onClick={handleOpen}>Open modal</Button>
//       <Modal
//         aria-labelledby="transition-modal-title"
//         aria-describedby="transition-modal-description"
//         open={open}
//         onClose={handleClose}
//         closeAfterTransition
//         BackdropComponent={Backdrop}
//         BackdropProps={{
//           timeout: 500,
//         }}
//       >
//         <Fade in={open}>
//           <Box sx={style}>
//             <Typography id="transition-modal-title" variant="h6" component="h2">
//               Text in a modal
//             </Typography>
//             <Typography id="transition-modal-description" sx={{ mt: 2 }}>
//               Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
//             </Typography>
//           </Box>
//         </Fade>
//       </Modal>
//     </div>
//   );
// }
