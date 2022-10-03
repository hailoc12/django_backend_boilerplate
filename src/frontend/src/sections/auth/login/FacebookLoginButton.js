import { Button } from '@mui/material';

import FacebookIcon from '@mui/icons-material/Facebook';
import { styled } from '@mui/material/styles';
import { useState } from 'react';
import { LoadingButton } from '@mui/lab';
import useAuth from 'src/hooks/useAuth';
import { useRouter } from 'next/router';
import { PATH_PAGE } from 'src/routes/paths';

const FBButton = styled(LoadingButton)(({ theme }) => ({
  // color: theme.palette.getContrastText(purple[500]),
  backgroundColor: "#1675d1",
  '&:hover': {
    backgroundColor: "#1463b3",
  },
}));


export default function FacebookLoginButton(props) {
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const router = useRouter();

  const handleSuccess = () => {
    setLoading(false);
    router.replace(PATH_PAGE.home);
  }

  const handleFailure = () => {
    setLoading(false);
  }

  const handleSignInWithFacebook = async (e) => {
    setLoading(true);
    login(handleSuccess, handleFailure);
  }

  return (
    <FBButton variant="contained" startIcon={<FacebookIcon/>} size="large" onClick={handleSignInWithFacebook} loading={loading}>Đăng nhập bằng Facebook</FBButton>
  )
}