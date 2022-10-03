import Page from '../components/Page';
import Layout from '../layouts';
import { styled } from '@mui/material/styles';
import RenderPageContent from 'src/sections/render/RenderPageContent';

const RootStyle = styled('div')(() => ({
  height: '100%',
}));

RenderPage.getLayout = function getLayout(page) {
  return <Layout variant="main">{page}</Layout>;
};

export default function RenderPage() {
    
  return (
    <Page title="Tạo tranh">
      <RootStyle>
        <RenderPageContent/>
      </RootStyle>
    </Page>
  )
}