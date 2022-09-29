import { Typography, useTheme } from "@mui/material";
import { useEffect, useState } from "react";
import { getPocket } from "src/services/PocketService";


export default function AccountBalance() {
    const [balance, setBalance] = useState(null);
    const theme = useTheme();

    useEffect(() => {
        (async () => {
            const res = await getPocket();
            setBalance(res[0].balance);
        })();
    }, [])

    return (
        <Typography variant="body2">Còn:{' '}<span style={{color: theme.palette.primary.main}}>{balance !== null && balance !== undefined ? balance : '-'}</span>{' '}điểm</Typography>
    )
}