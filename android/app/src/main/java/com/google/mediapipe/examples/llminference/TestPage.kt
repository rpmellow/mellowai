package com.google.mediapipe.examples.llminference

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color

@Composable
fun TestPage() {
 Box(modifier = Modifier
 .fillMaxSize()
 .background(Color.Pink)) {
            modifier = Modifier.fillMaxSize()
        )
        Text(
            text = "Hello, World!",
            modifier = Modifier.align(Alignment.Center)
        )
    }
}
