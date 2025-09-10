package com.example.homeautomation

import android.content.Context
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.homeautomation.databinding.ActivityMainBinding
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.logging.HttpLoggingInterceptor
import java.util.concurrent.TimeUnit

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    // SharedPreferences key
    private val PREFS = "home_prefs"
    private val KEY_IP = "pi_ip"

    // OkHttp client (simple GET)
    private val client by lazy {
        val logging = HttpLoggingInterceptor()
        logging.level = HttpLoggingInterceptor.Level.BASIC
        OkHttpClient.Builder()
            .addInterceptor(logging)
            .callTimeout(6, TimeUnit.SECONDS)
            .connectTimeout(4, TimeUnit.SECONDS)
            .build()
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        // load saved IP if any
        val prefs = getSharedPreferences(PREFS, Context.MODE_PRIVATE)
        binding.etIp.setText(prefs.getString(KEY_IP, ""))

        binding.saveBtn.setOnClickListener {
            val ip = binding.etIp.text.toString().trim()
            if (ip.isNotEmpty()) {
                prefs.edit().putString(KEY_IP, ip).apply()
                Toast.makeText(this, "Saved IP: $ip", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "Enter valid Pi IP", Toast.LENGTH_SHORT).show()
            }
        }

        // attach click listeners - endpoints chosen /loadX/on /loadX/off and /loads/on /loads/off
        binding.btnLoad1On.setOnClickListener { sendCommand("load1/on") }
        binding.btnLoad1Off.setOnClickListener { sendCommand("load1/off") }

        binding.btnLoad2On.setOnClickListener { sendCommand("load2/on") }
        binding.btnLoad2Off.setOnClickListener { sendCommand("load2/off") }

        binding.btnLoad3On.setOnClickListener { sendCommand("load3/on") }
        binding.btnLoad3Off.setOnClickListener { sendCommand("load3/off") }

        binding.btnLoad4On.setOnClickListener { sendCommand("load4/on") }
        binding.btnLoad4Off.setOnClickListener { sendCommand("load4/off") }

        binding.btnAllOn.setOnClickListener { sendCommand("loads/on") }
        binding.btnAllOff.setOnClickListener { sendCommand("loads/off") }
    }

    private fun sendCommand(endpoint: String) {
        val ip = binding.etIp.text.toString().trim()
        if (ip.isEmpty()) {
            Toast.makeText(this, "Please enter Raspberry Pi IP and Save it.", Toast.LENGTH_SHORT).show()
            return
        }

        val url = "http://$ip:5000/$endpoint" // default port 5000 for Flask example
        // Launch network call in IO dispatcher
        CoroutineScope(Dispatchers.IO).launch {
            try {
                val request = Request.Builder()
                    .url(url)
                    .get()
                    .build()

                client.newCall(request).execute().use { response ->
                    if (response.isSuccessful) {
                        runOnUiThread {
                            Toast.makeText(this@MainActivity, "OK: $endpoint", Toast.LENGTH_SHORT).show()
                        }
                    } else {
                        runOnUiThread {
                            Toast.makeText(this@MainActivity, "Error ${response.code}: ${response.message}", Toast.LENGTH_LONG).show()
                        }
                    }
                }
            } catch (e: Exception) {
                e.printStackTrace()
                runOnUiThread {
                    Toast.makeText(this@MainActivity, "Request failed: ${e.message}", Toast.LENGTH_LONG).show()
                }
            }
        }
    }
}
