import { TextField, InputAdornment } from '@mui/material';
import { styled } from '@mui/material/styles';

const StyledTextField = styled(TextField)({
  '& input:valid + fieldset': {
    borderWidth: 0,
  },
  '& input:invalid + fieldset': {
    borderWidth: 0,
  },
  '& .MuiOutlinedInput-root': {
    color: 'black',
    '&.Mui-focused fieldset': {
      borderWidth: 0,
    },
  },
});


export const PromptTextField = ({value, onChange}) => {

  return (
    <StyledTextField
      placeholder="Một chú gà đang đi trong sân trong một ngày nắng đẹp"
      variant="outlined"
      InputProps={{
          startAdornment: <InputAdornment position="start">Tôi muốn vẽ: </InputAdornment>,
      }}
      style={{backgroundColor: 'white', borderRadius: '20px', width: '100%'}}
      value={value}
      onChange={onChange}
    />
  )
}
